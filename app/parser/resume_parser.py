
import re
import spacy
import pdfplumber
import docx2txt
import pytesseract
from PIL import Image

class ResumeParser:

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

        self.skills_db = [
            "python", "fastapi", "django", "flask",
            "react", "nodejs", "docker", "kubernetes",
            "aws", "machine learning", "deep learning",
            "sql", "mongodb", "nlp", "tensorflow",
            "pytorch", "opencv", "git"
        ]

    def extract_text(self, file_path):
        if file_path.endswith(".pdf"):
            text = ""
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
            return text

        elif file_path.endswith(".docx"):
            return docx2txt.process(file_path)

        elif file_path.endswith((".png", ".jpg", ".jpeg")):
            image = Image.open(file_path)
            return pytesseract.image_to_string(image)

        else:
            raise Exception("Unsupported file format")

    def extract_email(self, text):
        match = re.search(r'[\w\.-]+@[\w\.-]+', text)
        return match.group(0) if match else None

    def extract_phone(self, text):
        match = re.search(r'(\+\d{1,3}[- ]?)?\d{10}', text)
        return match.group(0) if match else None

    def extract_name(self, text):
        doc = self.nlp(text[:1000])

        for ent in doc.ents:
            if ent.label_ == "PERSON":
                return ent.text

        return None

    def extract_skills(self, text):
        text = text.lower()

        found = []

        for skill in self.skills_db:
            if skill.lower() in text:
                found.append(skill)

        return list(set(found))

    def extract_education(self, text):
        education_keywords = [
            "Bachelor", "Master", "B.Tech",
            "M.Tech", "BSc", "MSc", "MBA"
        ]

        education = []

        lines = text.split("\n")

        for line in lines:
            for keyword in education_keywords:
                if keyword.lower() in line.lower():
                    education.append(line.strip())

        return education

    def extract_experience(self, text):
        experience = []

        lines = text.split("\n")

        for line in lines:
            if "experience" in line.lower():
                experience.append(line.strip())

        return experience

    def parse_resume(self, file_path):
        text = self.extract_text(file_path)

        return {
            "name": self.extract_name(text),
            "email": self.extract_email(text),
            "phone": self.extract_phone(text),
            "skills": self.extract_skills(text),
            "education": self.extract_education(text),
            "experience": self.extract_experience(text)
        }
