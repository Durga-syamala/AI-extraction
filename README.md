
# AI Extraction Service

An AI-powered service that converts unstructured text into validated structured data using Groq, Python, and Pydantic.

## Features

- Extracts person details from natural language.
- Uses Groq AI with function/tool calling.
- Validates extracted data using Pydantic.
- Handles missing and invalid information.
- Provides REST API using FastAPI.
- Includes automated tests using Pytest.

## Extracted Fields

- Name
- Age
- Email
- Profession
- Company

## Project Structure

```text
ai-extraction-service/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── config.py
│   ├── extractor.py
│   ├── tools.py
│   └── exceptions.py
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_api.py
│   └── test_extractor.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

```bash
python -m venv venv
```

Activate virtual environment on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Add Groq API key to `.env`:

```env
GROQ_API_KEY=your_groq_api_key
```

## Run the Application

```bash
python -m uvicorn app.main:app --reload
```

Open API documentation:

http://127.0.0.1:8000/docs

## API Endpoint

POST `/extract`

Example request:

```json
{
  "text": "My name is Syamala. I am 25 years old and work as a Developer at ABC Tech. My email is syamala@gmail.com."
}
```

## Run Tests

```bash
python -m pytest -v
```

## Technologies

- Python
- Groq API
- Pydantic
- FastAPI
- Pytest
