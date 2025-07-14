FROM blender:3.6

COPY cleanup_and_export.py /app/
WORKDIR /app

CMD ["blender", "--background", "--python", "cleanup_and_export.py"]
