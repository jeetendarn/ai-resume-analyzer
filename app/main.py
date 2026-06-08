from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates

from app.parser.resume_parser import ResumeParser
from app.utils.exporter import export_json, export_csv

import tempfile
import os

app = FastAPI(
    title="AI Resume Parser API",
    description="Production-ready Resume Parser API using OCR + NLP + FastAPI",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

parser = ResumeParser()


# FRONTEND UI
@app.get("/")
async def frontend(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# PARSE RESUME
@app.post("/parse")
async def parse_resume(file: UploadFile = File(...)):
    try:

        suffix = file.filename.split(".")[-1]

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=f".{suffix}"
        ) as temp:

            temp.write(await file.read())

            temp_path = temp.name

        data = parser.parse_resume(temp_path)

        os.remove(temp_path)

        return JSONResponse(content=data)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# EXPORT JSON
@app.post("/export/json")
async def export_json_api(file: UploadFile = File(...)):

    suffix = file.filename.split(".")[-1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=f".{suffix}"
    ) as temp:

        temp.write(await file.read())

        temp_path = temp.name

    data = parser.parse_resume(temp_path)

    export_path = export_json(data)

    return FileResponse(
        export_path,
        filename="resume_data.json"
    )


# EXPORT CSV
@app.post("/export/csv")
async def export_csv_api(file: UploadFile = File(...)):

    suffix = file.filename.split(".")[-1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=f".{suffix}"
    ) as temp:

        temp.write(await file.read())

        temp_path = temp.name

    data = parser.parse_resume(temp_path)

    export_path = export_csv(data)

    return FileResponse(
        export_path,
        filename="resume_data.csv"
    )