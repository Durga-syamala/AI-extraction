from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.models import ExtractionRequest, ExtractionResponse
from app.extractor import extract_person
from app.exceptions import AIServiceError

app = FastAPI(
    title="AI Extraction Service",
    description="Extract structured person information from unstructured text",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "AI Extraction Service is running"}


@app.post("/extract", response_model=ExtractionResponse)
def extract(request: ExtractionRequest):
    try:
        person = extract_person(request.text)

        return ExtractionResponse(
            success=True,
            data=person,
            errors=[]
        )

    except AIServiceError as error:
        error_response = ExtractionResponse(
            success=False,
            data=None,
            errors=[str(error)]
        )

        return JSONResponse(
            status_code=502,
            content=error_response.model_dump(mode="json")
        )