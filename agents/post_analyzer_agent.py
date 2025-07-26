import os
import google.generativeai as genai
import re

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def extract_links(text):
    return re.findall(r'(https?://\S+)', text)

def summarize_post(title, body):
    print("Summarizing post...")
    prompt = f"Summarize this Reddit post:\n\nTitle: {title}\n\nBody: {body}"
    response = model.generate_content(prompt)
    return response.text

def analyze_post(title, body):
    links = extract_links(body)
    summary = summarize_post(title, body)
    return summary, links
