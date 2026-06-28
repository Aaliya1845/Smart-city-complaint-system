import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_complaint(complaint):

    prompt = f"""
You are an AI Smart City Complaint Officer.

Analyze this complaint.

Complaint:
{complaint}

Return ONLY in this format.

Category:
Priority:
Department:
Summary:

Priority should be one of:
Low
Medium
High
Emergency

Department examples:
Sanitation
Water Department
Road Department
Electricity Department
Traffic Police
Municipal Corporation
"""

    response = model.generate_content(prompt)

    return response.text
