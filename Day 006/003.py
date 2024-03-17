import pyttsx3

def read_words_aloud():
    engine = pyttsx3.init()
    words = input("Hello, I am Jarvis. How may I assist you today? ")
    engine.say(words)
    engine.runAndWait()

if __name__ == "__main__":
    read_words_aloud()
