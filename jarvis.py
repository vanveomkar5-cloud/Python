# import speech_recognition as sr
# pttsx3
# pyaudio
import webbrowser
import datetime

def jarvis():
    print("Hello! I am Jarvis...")
    print("Available Commands")
    print("1. Google\n2. YouTube\n3. Time\n4. Exit")

    while True:
        command = input("\nEnter Command: ").lower()

        if command == "google":
            print("Openning Google...")
            webbrowser.open("https://www.google.com")

        elif command == "youtube":
            print("Openning YouTube...")
            webbrowser.open("https://www.youtube.com")

        elif command == "time":
            print("Openning YouTube...")
            webbrowser.open("https://www.time.com")

        elif command == "exit":
            break

        else:
            print("Command Not Found!!")


jarvis()