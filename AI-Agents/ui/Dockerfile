FROM python:3.10

WORKDIR /app
COPY streamlit_input.py .
RUN pip install streamlit requests

CMD ["streamlit", "run", "streamlit_input.py", "--server.port=8501", "--server.enableCORS=false"]
