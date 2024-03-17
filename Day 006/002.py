def read_words():
    words = input("Hello, I am Jarvis. How may I assist you today? ").split()
    return words

if __name__ == "__main__":
    words = read_words()
    print("Words entered:", words)
