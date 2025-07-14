import os
import sys
from datetime import datetime

OUTPUT_DIR = "./shared/output"

def generate_dummy_stl(prompt, output_path):
    # This is a placeholder. Replace with AI model inference.
    stl_content = f"""solid TESTING {prompt}
  facet normal 0 0 0
    outer loop
      vertex 0 0 0
      vertex 1 0 0
      vertex 0 1 0
    endloop
  endfacet
endsolid {prompt}
"""
    with open(output_path, "w") as f:
        f.write(stl_content)

def main():
    # Get prompt from command line or environment
    prompt = os.environ.get("PROMPT")
    if not prompt and len(sys.argv) > 1:
        prompt = sys.argv[1]
    if not prompt:
        print("No prompt provided.")
        sys.exit(1)

    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prompt.replace(' ', '_')}_{timestamp}.stl"
    output_path = os.path.join(OUTPUT_DIR, filename)

    print(f"Generating STL for prompt: {prompt}")
    generate_dummy_stl(prompt, output_path)
    print(f"Saved: {output_path}")

if __name__ == "__main__":
    main()