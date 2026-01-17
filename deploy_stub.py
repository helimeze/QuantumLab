# Minimal SageMaker job+deploy example.
# Requires: pip install sagemaker boto3, and valid AWS credentials.
import os, sagemaker
from sagemaker.pytorch import PyTorch

ROLE = os.environ.get("SM_ROLE_ARN", "arn:aws:iam::<account-id>:role/<SageMakerRole>")
BUCKET = os.environ.get("SM_BUCKET", "your-bucket")
PREFIX = "aws-qc-starter"

est = PyTorch(
    entry_point="train.py",
    source_dir="sagemaker/src",
    role=ROLE,
    framework_version="2.2",
    py_version="py310",
    instance_type="ml.c5.large",
    instance_count=1,
    hyperparameters={"epochs": 1}
)
est.fit({"train": f"s3://{BUCKET}/{PREFIX}/train/"})
predictor = est.deploy(instance_type="ml.m5.large", initial_instance_count=1)
print("Endpoint:", predictor.endpoint_name)
print(predictor.predict({"inputs":[[0.0]*20]}))
