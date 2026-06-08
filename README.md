
# AI Resume Parser API

Production-ready AI Resume Parser API built using:

- FastAPI
- OCR (Tesseract)
- NLP (spaCy)
- Swagger Documentation
- Resume Export Features
- Frontend UI

---

## Features

✅ Extract Name  
✅ Extract Email  
✅ Extract Phone  
✅ Extract Skills  
✅ Extract Education  
✅ Extract Experience  
✅ OCR Support  
✅ PDF Support  
✅ DOCX Support  
✅ Image Resume Support  
✅ Swagger API Docs  
✅ JSON Export  
✅ CSV Export  
✅ Production Ready Architecture  

---

## Installation

```bash
git clone <repo>
cd ai_resume_parser_api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install spaCy model:

```bash
python -m spacy download en_core_web_sm
```

Run API:

```bash
uvicorn app.main:app --reload
```

---

## Swagger Documentation

Open:

http://127.0.0.1:8000/docs

---

## API Endpoints

### Parse Resume

POST `/parse`

### Export JSON

POST `/export/json`

### Export CSV

POST `/export/csv`

---

## Frontend UI

Open:

frontend/index.html

---

## Deployment

Recommended:

- Docker
- Render
- Railway
- AWS EC2
- DigitalOcean

---

## Folder Structure

```bash
ai_resume_parser_api/
│
├── app/
│   ├── main.py
│   ├── parser/
│   └── utils/
│
├── frontend/
├── requirements.txt
└── README.md
```

---

## Freelancing Tips

You can sell this as:

- HR Automation Tool
- ATS Resume Parser
- Recruitment SaaS
- Hiring Dashboard Backend

Add-ons you can charge for:

- LinkedIn Parsing
- AI Resume Scoring
- Candidate Ranking
- Job Matching
- Dashboard Analytics
