from google.cloud import aiplatform

"""
Register the model to Vertex AI.
"""

REGION = "us-central1"
PROJECT_ID = "rag-nick"
IMAGE_URL = "us-central1-docker.pkg.dev/rag-nick/huggingface-cloud"
REPO = "huggingface-cloud"


aiplatform.init(project=PROJECT_ID, location=REGION)

model = aiplatform.Model.upload(
    display_name="paraphrase-MiniLM",
    artifact_uri="gs://artifacts.rag-nick.appspot.com",
    serving_container_image_uri=f"{REGION}-docker.pkg.dev/{PROJECT_ID}/{REPO}/predictor1:latest",
    serving_container_environment_variables={
        "HF_TASK": "paraphrase",
        "VERTEX_CPR_WEB_CONCURRENCY": 1,
    },
)