import requests

def generate_fake_response(attacker_input: str) -> str:
    prompt = f"""
You are a fake Linux server being probed by an attacker over SSH.
The attacker entered: '{attacker_input}'
Respond like a realistic but fake Linux system trying to mislead the attacker.
Include believable output like fake directory listings or dummy secrets.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "[Error communicating with LLaMA via Ollama]"
