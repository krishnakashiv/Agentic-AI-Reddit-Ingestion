import os
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash-lite")

def scrape_url_text(url):
    try:
        resp = requests.get(url, timeout=5)
        soup = BeautifulSoup(resp.text, "html.parser")
        return soup.get_text()
    except Exception as e:
        return f"Failed to scrape: {e}"

def analyze_link(url):
    print(f"Analyzing link: {url}")
    text = scrape_url_text(url)
    prompt = f"Summarize the following information:\n\n{text}"
    try:
        response = model.generate_content(prompt)
        return {
            "url": url,
            "summary": response.text
        }
    except Exception as e:
        return {"url": url, "error": str(e)}
