import openai
import os
from flask import Flask, request, render_template

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def chat_with_gpt(prompt):
    """Generates a response using OpenAI API or a fallback if the API fails."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception:
        return "I'm always here to help, but it looks like I ran into an issue! Try again later."

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = chat_with_gpt(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
