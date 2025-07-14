AI-AGENTS/
├── docker-compose.yml
├── .env
├── n8n/
│   └── data/                  # n8n persistent storage
│   └── workflow.json          # n8n importable workflow
├── model_gen/
│   ├── Dockerfile             # Python with TripoSR
│   ├── generate_model.py
│   └── requirements.txt
│   └── output/                # Volume-shared STL output
├── blender/
│   ├── Dockerfile
│   ├── cleanup_and_export.py
│   └── output/                # Optional cleaned STL output
├── ui/
│   ├── Dockerfile
│   └── streamlit_input.py
├── shared/
│   └── output/                # Shared folder for generated files
└── README.md
