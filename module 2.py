# Install dependencies:
# pip install SpeechRecognition opencv-python pygame
import cv2
import speech_recognition as sr
import pygame
import time
import os

# Speech recognition function
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Could not understand the audio")
            return None
        except sr.RequestError:
            print("API unavailable")
            return None

# Simple dictionary for text-to-sign mapping
# Assume you have video files for each sign, e.g., "hello.mp4", "how.mp4", etc.
sign_language_dict = {
    "hello": "hello.mp4",
    "how": "how.mp4",
    "are": "are.mp4",
    "you": "you.mp4"
}

# Function to display sign language
def display_sign(video_file):
    # Using OpenCV or pygame to display videos
    cap = cv2.VideoCapture(video_file)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Sign Language', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def convert_speech_to_sign_language():
    # Step 1: Convert speech to text
    text = speech_to_text()
    
    if text:
        
        words = text.split()

        # Step 2: Display corresponding sign for each word
        for word in words:
            if word in sign_language_dict:
                video_file = sign_language_dict[word]
                print(f"Displaying sign for '{word}'")
                display_sign(video_file)
            else:
                print(f"Sign for '{word}' not found in dictionary")

if __name__ == "__main__":
    convert_speech_to_sign_language()

