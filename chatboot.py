import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import re
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speaking speed

# Set Google Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

WAKE_WORDS = ["hey assistant", "hello assistant"]

# Custom Responses
CUSTOM_RESPONSES = {
    # Example: "how to buy a house": "You can start by checking your credit score and getting pre-approved for a mortgage."
}

def clean_text(text):
    """Remove unwanted characters from text"""
    return re.sub(r"[*_`]", "", text).strip()

def speak(text):
    """Convert cleaned text to speech"""
    try:
        engine.say(clean_text(text))
        engine.runAndWait()
    except Exception as e:
        print(f"Speech error: {str(e)}")

def listen():
    """Capture voice input and return it as text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            text = recognizer.recognize_google(audio).lower()
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            print("Speech service is down.")
            return None
        except sr.WaitTimeoutError:
            return None

def ask_google_bard(question):
    """Send the question to Google Gemini API and get a response"""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(question)
        return response.text if response else "I couldn't find an answer."
    except Exception as e:
        return "I'm having trouble connecting to Google right now. Try again later."

def get_custom_response(query):
    """Check if query contains predefined customer support keywords."""
    for key, answer in CUSTOM_RESPONSES.items():
        if key in query:
            return answer
    return None

def wait_for_wake_word():
    """Wait for wake word once before starting the main loop"""
    speak("Hello, say 'Hey Assistant' to start.")
    while True:
        wake_word = listen()
        if wake_word and any(ww in wake_word for ww in WAKE_WORDS):
            speak("Yes, I'm listening!")
            return

def main():
    """Main function to interact with the user"""
    wait_for_wake_word()
    
    while True:
        command = listen()
        if command:
            if "exit" in command or "stop" in command:
                speak("Goodbye!")
                print("AI : Good Bye")
                break
            else:
                custom_response = get_custom_response(command)
                if custom_response:
                    print("AI:", custom_response)
                    speak(custom_response)
                else:
                    response = ask_google_bard(command)
                    cleaned_response = clean_text(response)
                    print("AI:", cleaned_response)
                    speak(cleaned_response)
        else:
            speak("I didn't catch that. Try again.")

if __name__ == "__main__":
    main()