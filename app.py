
import gradio as gr
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file or environment variables.")

genai.configure(api_key=GEMINI_API_KEY)



# Create the generative model
model = genai.GenerativeModel('gemini-1.5-flash')

def get_response(query, history):
    """
    Gets a response from the Gemini model.

    Args:
        query: The user's query.
        history: The conversation history.

    Returns:
        A string containing the model's response.
    """
    chat = model.start_chat(history=history)
    response = chat.send_message(query)
    return response.text

iface = gr.ChatInterface(
    fn=get_response,
    title="Gemini Q&A with History",
    description="Enter your query to get a response from the Gemini model.",
    chatbot=gr.Chatbot(height=600)
)

if __name__ == "__main__":
    iface.launch()
