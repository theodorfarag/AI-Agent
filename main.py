import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

parser = argparse.ArgumentParser(description='Chatbot')
parser.add_argument("user_prompt", type=str, help='User prompt that is given to the Gemini AI')
parser.add_argument("--verbose", '-v', action='store_true', help="Enable verbose output")
args = parser.parse_args()

load_dotenv()  

API_KEY = os.getenv('GEMINI_API_KEY')

if API_KEY == None:
    raise RuntimeError('No gemini API key is present! Make sure .env has API key')

client = genai.Client(api_key=API_KEY)

# This is where the history of messages will be saved
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

def main():
    print("Hello from ai-agent!")
    response = client.models.generate_content(
        model='gemini-2.5-flash', contents=messages
    )
    if response.usage_metadata is None:
        raise RuntimeError('API failed and was unable to register token count')
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    print('Response:')
    print(response.text)


if __name__ == "__main__":
    main()
