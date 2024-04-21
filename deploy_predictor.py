"""
This deploying file does not work on my local machine, but I was able to push the image manuelly.
"""


import os
from google.cloud.aiplatform.prediction import LocalModel
from predictor import HuggingFacePredictor
REGION = "us-central1"
PROJECT_ID = "rag-nick"

local_model = LocalModel.build_cpr_model(
    ".",
    f"{REGION}-docker.pkg.dev/{PROJECT_ID}/huggingface-cloud/huggingface-pipeline:py310-cpu-torch-2.2.0-transformers-4.38.1",
    predictor=HuggingFacePredictor,
    requirements_path="requirements.txt",
    base_image="--platform=linux/amd64 alvarobartt/torch-gpu:py310-cu12.3-torch-2.2.0 AS build",
)
local_model.push_image()