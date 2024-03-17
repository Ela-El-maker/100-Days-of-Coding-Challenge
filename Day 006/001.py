def read_words():
    words = input("Enter words separated by spaces: ").split()
    return words

def loud_words(words):
    return [word.upper() for word in words]

if __name__ == "__main__":
    words = read_words()
    loud_words_list = loud_words(words)
    print("Words entered (loud):", loud_words_list)
