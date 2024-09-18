from flask import Flask, render_template, jsonify
import speech_recognition as sr
import os

app = Flask(__name__)

# Simple dictionary for text-to-sign mapping
sign_language_dict = {
    "hello": "C:/Users/jeswi/Downloads/SIH2/hello.mp4",
    "welcome": "C:/Users/jeswi/Downloads/SIH2/welcome.mp4"
}

# Speech recognition function
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            return "error_unknown"
        except sr.RequestError:
            return "error_api"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech', methods=['POST'])
def recognize_speech():
    # Convert speech to text
    text = speech_to_text()
    
    if text in sign_language_dict:
        return jsonify({'text': text, 'video': sign_language_dict[text]})
    elif text == "error_unknown":
        return jsonify({'error': 'Could not understand the audio. Please try again.'})
    elif text == "error_api":
        return jsonify({'error': 'Speech Recognition API is unavailable.'})
    else:
        return jsonify({'error': f"Sign for '{text}' not found."})

if __name__ == "__main__":
    app.run(debug=True)
