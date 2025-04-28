# Voice Assistant Project

This is a simple voice assistant that listens for a wake word and then processes voice commands. It uses various libraries to recognize speech, convert text to speech, and interact with the Google Gemini API (formerly known as Google Bard) for generating responses to user queries. The assistant also has predefined responses for specific commands.

## Features
- **Voice Command Recognition:** Listens for voice input using speech recognition.
- **Text-to-Speech:** Converts responses to speech using `pyttsx3`.
- **Google Gemini Integration:** Sends queries to the Google Gemini API and returns responses.
- **Custom Responses:** Can be customized with predefined responses for specific queries.
- **Wake Word:** Waits for a wake word (e.g., "Hey Assistant") to activate the assistant.

## Requirements
Before running this project, you need to install the following Python packages:

- `speech_recognition`: For recognizing speech and converting it to text.
- `pyttsx3`: For text-to-speech conversion.
- `google-generativeai`: For interacting with the Google Gemini API.
- `python-dotenv`: To load environment variables from a `.env` file.

You can install the necessary packages using the following command:

```bash
pip install speech_recognition pyttsx3 google-generativeai python-dotenv
