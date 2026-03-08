# AI Chatbot (Streamlit + Gemini)

Simple AI chatbot built with **Python and Streamlit**, integrated with the **Google Gemini API** to generate responses in real time.

## Tech Stack

- **Python** – main programming language
- **Streamlit** – framework for building the web interface
- **Google Gemini API** – AI model used to generate responses
- **python-dotenv** – environment variable management for API keys

## How it works

The user sends a message through the chat interface.  
The application sends the message to the **Gemini model**, which generates a response that is displayed back in the chat.

## Run locally

Install dependencies:

```bash
pip install -r requirements.txt
```
Create a .env file:

```
GOOGLE_API_KEY=your_api_key
```

Run the app:
```
streamlit run main.py
```
