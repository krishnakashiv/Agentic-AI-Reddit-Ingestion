from ollama import chat
import json

def is_post_relevant(title: str, body: str, model="gemma:2b"):
    print("Checking post relevancy...")

    prompt = f"""
    You are a helpful assistant. Your job is to decide whether a Reddit post is related to AI, cybersecurity, or vulnerabilities.

    Return your answer in strict JSON format, like this:
    {{{{"relevant": true, "how": "explanation of why it's relevant"}}}}
    or
    {{{{"relevant": false, "how": "explanation of why it's not relevant"}}}}

    ONLY return valid JSON. Do NOT include any extra text or commentary.

    ---
    Title: {title}

        Example:
        Example 1:
    Title: OpenAI releases new GPT-5 security patch
    Body: The patch addresses prompt injection issues in chat completions.

    Response:
    {{"relevant": true, "how": "This is about a vulnerability patch in an AI model"}}

    Example 2:
    Title: Whats your favorite game engine?
    Body: I like Unreal Engine 5.
    Response:
    {{"relevant": false, "how": "This is a general tech discussion, not related to AI security or vulnerabilities."}}

    """

    response = chat(model=model, messages=[{"role": "user", "content": prompt}])
    try:
        data = json.loads(response["message"]["content"])
        relevant = data.get("relevant", False)
        explanation = data.get("how", "")
        print(relevant, explanation)
    except json.JSONDecodeError:
        relevant = False
        explanation = "Invalid JSON format or model did not follow instructions."
    return relevant, explanation
   

