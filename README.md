# Gemini Q&A with History

This is a simple web application that allows you to have a conversation with the Gemini Pro model. It uses the Gradio library to create the user interface and keeps track of the conversation history.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2.  **Install the required Python libraries:**
    The packages at least to install are: pip install -q -U google-generativeai
    ```bash
    pip install -q -U google-generativeai
    pip install gradio
    pip install dotenv
    ```
    For the full required packages, please use below command
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    Create a file named `.env` in the root of the project and add your Gemini API key to it:
    ```
    GEMINI_API_KEY=YOUR_API_KEY
    ```
    Replace `YOUR_API_KEY` with your actual API key.

## Usage

1.  **Run the application:**
    ```bash
    python app.py
    ```

2.  **Open the application in your browser:**
    The application will be running at a local URL, which will be displayed in your terminal (usually `http://127.0.0.1:7860`). Open this URL in your web browser to start interacting with the Gemini model.
