# blender/render_preview.py

import bpy
import os

# Clear default scene
bpy.ops.wm.read_factory_settings(use_empty=True)

# Import STL file
model_path = "/app/output/result.stl"
bpy.ops.import_mesh.stl(filepath=model_path)
obj = bpy.context.selected_objects[0]

# Add lighting
light_data = bpy.data.lights.new(name="light", type='POINT')
light_object = bpy.data.objects.new(name="light", object_data=light_data)
bpy.context.collection.objects.link(light_object)
light_object.location = (3, -3, 5)

# Add camera
cam = bpy.data.objects.new("Camera", bpy.data.cameras.new("Camera"))
bpy.context.scene.collection.objects.link(cam)
cam.location = (3, -3, 2)
cam.rotation_euler = (1.2, 0, 0.9)
bpy.context.scene.camera = cam

# Set render resolution
bpy.context.scene.render.resolution_x = 800
bpy.context.scene.render.resolution_y = 800

# Set output path
bpy.context.scene.render.filepath = "/app/output/preview.png"

# Add smooth shading
bpy.context.view_layer.objects.active = obj
bpy.ops.object.shade_smooth()

# Set render engine to CYCLES
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.device = 'CPU'

# Render
bpy.ops.render.render(write_still=True)

print("✅ Preview image generated")
