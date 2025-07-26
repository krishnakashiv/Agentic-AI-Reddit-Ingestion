from ollama import chat

def is_post_relevant(title: str, body: str, model="gemma:2b"):
    print("Checking post relevancy...")
    prompt = f"Is this Reddit post about AI, cybersecurity, or vulnerabilities?\n\nTitle: {title}\n\nBody: {body}\n\nReply only with 'Yes' or 'No'."
    response = chat(model=model, messages=[{"role": "user", "content": prompt}])
    
    
    return 'yes' in response['message']['content'].lower()
