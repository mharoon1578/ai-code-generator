import os
import argparse
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "mixtral-8x7b-32768"

def generate_code(prompt, debug=False):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 512,
        "stop": None
    }
    
    response = requests.post(API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        code = response.json()["choices"][0]["message"]["content"]
        if debug:
            print("\n[DEBUG] Generated Code:")
            print("=" * 50)
        print(code)
    else:
        print(f"Error: {response.status_code}, {response.json()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI-Powered Code Generator using Groq API")
    parser.add_argument("--prompt", type=str, required=True, help="Coding request prompt")
    parser.add_argument("--debug", action="store_true", help="Enable debugging mode")
    args = parser.parse_args()
    
    generate_code(args.prompt, args.debug)
