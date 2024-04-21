# AI_Highlighter

## Instalation
- gcloud config list project -> choose the project
- arch -arm64 brew install git-lfs -> install lfs -> git large file storage
- git lfs install -> install lfs

## Creating Customized Repository and push the predictor
- Create an artifact registry: gcloud artifacts repositories create huggingface-cloud --repository-format docker --location us-central1
- Authenticate this repository: gcloud auth configure-docker us-central1-docker.pkg.dev
- Build the docker image locally: docker build -t us-central1-docker.pkg.dev/rag-nick/huggingface-cloud/predictor1:latest .
- Push the image to the artifact registry: docker push us-central1-docker.pkg.dev/rag-nick/huggingface-cloud/predictor1:latest


## Clone the model
- git clone <MODEL URL>, example: git clone https://huggingface.co/sentence-transformers/paraphrase-MiniLM-L6-v2
- Compress the model: tar zcvf model.tar.gz --exclude flax_model.msgpack --exclude pytorch_model.bin --exclude rust_model.ot *
- The compressed model will be stored in model.tar.gz and then it will be stored in google storage

## Store the model in cloud
- gcloud config set storage/parallel_composite_upload_enabled True -> enable parallel upload
- Upload the model to google stroage: gcloud storage cp model.tar.gz gs://artifacts.rag-nick.appspot.com -> upload the model
- Register the model from google storage to vertext ai: python3 register_model.py