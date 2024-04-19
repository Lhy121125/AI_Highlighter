# AI_Highlighter

## Instalation
- gcloud config list project -> choose the project
- arch -arm64 brew install git-lfs -> install lfs -> git large file storage
- git lfs install -> install lfs

## Creating Customized Repository
- Create an artifact registry: gcloud artifacts repositories create huggingface-cloud --repository-format docker --location us-central1
- Authenticate this repository: gcloud auth configure-docker us-central1-docker.pkg.dev


