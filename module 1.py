import cv2
import speech_recognition as sr
import pygame
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
sign_language_dict = {
    "hello": "C:/Users/jeswi/Downloads/SIH2/hello.mp4",
    "welcome": "C:/Users/jeswi/Downloads/SIH2/welcome.mp4"
}

# Function to display sign language using OpenCV
def display_sign_opencv(video_file):
    if not os.path.exists(video_file):
        print(f"Error: Video file '{video_file}' does not exist.")
        return

    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        print(f"Error: Unable to open video file '{video_file}'.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Sign Language', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to display sign language using Pygame
def display_sign_pygame(video_file):
    if not os.path.exists(video_file):
        print(f"Error: Video file '{video_file}' does not exist.")
        return

    pygame.init()
    cap = cv2.VideoCapture(video_file)

    # Set up Pygame display
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    screen = pygame.display.set_mode((width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert color
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                return
    pygame.time.wait(display_duration * 1000)
    cap.release()
    pygame.quit()

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
                # Uncomment the method you want to use
                # display_sign_opencv(video_file)
                display_sign_pygame(video_file)
            else:
                print(f"Sign for '{word}' not found in dictionary")

if __name__ == "__main__":
    convert_speech_to_sign_language()
