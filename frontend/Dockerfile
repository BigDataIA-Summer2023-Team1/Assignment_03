FROM python:3.10.6-slim
# Pull the base docker image of python with tag 3.10.6-slim

RUN pip install --upgrade pip
# Upgrade pip package

WORKDIR /app
# Change the working dir inside the container - cd /app

COPY  main.py requirements.txt img_embeddings.json azure.py files.json ./
COPY pages ./pages
COPY fashion_dataset ./fashion_dataset
COPY output ./output
COPY upload_files ./upload_files
# Copy main.py as source cod and req.txt as dependency

RUN pip install -r requirements.txt
# Install the dependency

### Container Env same as local at this point
EXPOSE 8090

CMD ["streamlit", "run", "main.py", "--server.port", "8090"]
