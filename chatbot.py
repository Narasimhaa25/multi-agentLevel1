import os
import re
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import datetime

# 🔹 Load environment variables from .env
load_dotenv()

# 🔑 Configure Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

genai.configure(api_key=api_key)

# 🔹 Choose Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# 🔹 Predefined prompts for mandatory use cases
PREDEFINED_PROMPTS = {
    "what are the colors in a rainbow": "List the colors in a rainbow step-by-step.",
    "tell me why the sky is blue": "Explain why the sky appears blue, step by step.",
    "which planet is the hottest": "Identify the hottest planet in our solar system and explain why."
}

# 🔹 Log file
LOG_FILE = "logs.txt"

def log_interaction(user_input, bot_reply):
    """Append conversation to logs.txt with timestamp."""
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] You: {user_input}\n")
        f.write(f"[{timestamp}] Bot: {bot_reply}\n\n")

def is_math_question(user_input):
    """Detect simple arithmetic expressions."""
    return bool(re.search(r"\b\d+\s*[\+\-\*/]\s*\d+\b", user_input))

def ask_llm(prompt):
    """Generate response from Gemini LLM with error handling."""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

def chatbot():
    """Interactive CLI chatbot loop."""
    print("🤖 Smart Assistant (Level 1 - Gemini). Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            break

        # Check for math question
        if is_math_question(user_input):
            bot_reply = "I cannot perform calculations. Please use a calculator."
        # Check for predefined prompt
        elif user_input in PREDEFINED_PROMPTS:
            bot_reply = ask_llm(PREDEFINED_PROMPTS[user_input])
        # General fallback
        else:
            bot_reply = ask_llm(f"Answer this question step-by-step and clearly: {user_input}")

        # Print and log
        print("Bot:", bot_reply, "\n")
        log_interaction(user_input, bot_reply)

if __name__ == "__main__":
    chatbot()