
"""This project I have created is designed so that whenever you're working on your machine,
 you can simply call it and ask it to perform tasks like opening Google or
 answering any type of question. I know it's not an advanced or perfect project, 
 but I wanted to try something new and create this AI assistant."""

#     C A L L I N G   THE  S I R I 

import speech_recognition as sr
import webbrowser
import pyttsx3
# pip install pocketsphinx  # Required for offline speech recognition

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    # Initial greetings
    speak("Hello")
    print("Hello")
    speak("Initializing Siri...")
    print("Initializing Siri...")
    print("... Please wait...")

    # Function to process tasks based on the recognized command
    def Process_task(command):
        if "open" in command.lower():  # Check if the command is for opening a website
            if "open google" in command:
                webbrowser.open("https://google.com")  # Open Google
                print("Opening Google...")
                speak("Opening Google.")
            elif "open instagram" in command:
                webbrowser.open("https://instagram.com")  # Open Instagram
                print("Opening Instagram...")
                speak("Opening Instagram.")
            elif "open linkedin" in command:
                webbrowser.open("https://linkedin.com")  # Open LinkedIn
                print("Opening LinkedIn...")
                speak("Opening LinkedIn.")
            elif "open facebook" in command:
                webbrowser.open("https://facebook.com")  # Open Facebook
                print("Opening Facebook...")
                speak("Opening Facebook.")
            elif "open youtube" in command:
                webbrowser.open("https://youtube.com")  # Open YouTube
                print("Opening YouTube...")
                speak("Opening YouTube.")
        elif "play" in command.lower():  # Check if the command is for playing a song
            webbrowser.open("https://youtu.be/P4FBIZiieOo?si=rfimImSC77puHRsR")  # Play a specific song
            print("Playing song...")
            speak("Playing song...")
        else:  # For other commands, search on Google
            webbrowser.open(f"https://www.google.com/search?q={command}")
            speak(f"Searching Google for {command}")

    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=2)  # Adjust for ambient noise
                print("Listening...")

                # Listen for audio input
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                print("Recognizing...")

                # Recognize wake word
                wake_word = recognizer.recognize_google(audio)
                # word = recognizer.recognize_google(audio)  # Uncomment if needed

                if "siri" in wake_word.lower():  # If the wake word "Siri" is detected
                    print(f"You said: {wake_word}")
                    print("Yes, I'm listening...")
                    speak("Yes, I'm listening. What can I do for you?")
                    
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        recognizer.adjust_for_ambient_noise(source, duration=2)  # Adjust again for noise
                        audio_command = recognizer.listen(source, timeout=5, phrase_time_limit=5)  # Listen for command
                        
                        # Recognize the spoken command
                        command = recognizer.recognize_google(audio_command).lower()
                        
                        if "stop" in command:  # Stop execution if the user says "stop"
                            print("Okay, deactveting siri.")
                            print("have a nice day.")
                            speak("Okay, deactveting siri.")
                            speak(" have a nice day.")
                            break

                        print(f"You said: {command}") 
                        Process_task(command)  # Process the recognized command

        except sr.UnknownValueError:  # Handle cases where the speech is not understood
            print("Sorry, I could not understand the audio.")
            speak("Sorry, I could not understand that. Please try again.")
        except sr.RequestError as e:  # Handle errors with the speech recognition service
            print(f"Could not request results from the recognition service; {e}")
            speak("There is an issue with the recognition service.")
        except sr.WaitTimeoutError:  # Handle timeout errors
            print("")
        except Exception as e:  # Handle unexpected errors
            print(f"An unexpected error occurred: {e}")
            speak("An unexpected error occurred.")
 
         