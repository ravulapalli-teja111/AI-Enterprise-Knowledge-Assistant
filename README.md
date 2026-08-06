# AI Enterprise Knowledge Assistant

## Phase 1 - Azure AI Chatbot Foundation

A FastAPI application integrated with Azure AI Foundry and GPT-5-mini.

## Architecture

User
 |
FastAPI
 |
OpenAI SDK
 |
Azure AI Foundry
 |
GPT-5-mini


## Features Completed

- FastAPI backend
- Azure AI Foundry integration
- GPT-5-mini deployment
- Chat API endpoint
- Environment-based configuration
- Swagger API documentation

## Tech Stack

- Python
- FastAPI
- Azure AI Foundry
- Azure OpenAI SDK

## Run Locally

Create virtual environment:

python -m venv .venv

Activate:

Windows:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run:

uvicorn app.main:app --reload

API Documentation:

http://localhost:8000/docs