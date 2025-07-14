# model_gen/generate_model.py

import sys
import torch
from transformers import TripoSRPipeline
from pathlib import Path

def generate(prompt: str, output_path: str = "output/result.stl"):
    print(f"Generating model for prompt: '{prompt}'")

    # Load pipeline
    pipe = TripoSRPipeline.from_pretrained(
        "stabilityai/TripoSR",
        torch_dtype=torch.float16,
        variant="fp16"
    ).to("cuda" if torch.cuda.is_available() else "cpu")

    # Generate the mesh
    result = pipe(prompt)
    mesh = result.meshes[0]

    # Save the output
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    mesh.export(str(output_path))

    print(f"✅ Model saved to: {output_path}")
    return output_path

if __name__ == "__main__":
    # Get prompt from CLI arg or use default
    user_prompt = sys.argv[1] if len(sys.argv) > 1 else "A spiral vase"
    generate(user_prompt)
