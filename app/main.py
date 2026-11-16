
import os

from fastapi import FastAPI

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

app = FastAPI(
    title="GitOps Kubernetes API",
    description="API demonstrativa para um projeto de CI/CD e GitOps.",
    version=APP_VERSION,
)


@app.get("/")
def root():
    return {
        "application": "GitOps Kubernetes API",
        "version": APP_VERSION,
        "message": "Application running successfully",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": APP_VERSION,
    }
