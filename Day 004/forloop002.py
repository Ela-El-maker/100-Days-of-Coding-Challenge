text = """Python is powerful... and fast
plays well with others
runs everywhere
is friendly & easy to learn
is Open
These are some of the reasons people who use 
Python would rather not use anything else"""

# Step 1: Split the text into words
words = text.split()

# Step 2: Standardize the words (lowercase and remove punctuation)
standardized_words = []
for word in words:
    # Remove punctuation
    word = ''.join(char for char in word if char.isalnum())
    # Convert to lowercase
    word = word.lower()
    standardized_words.append(word)

# Step 3: Filter out words longer than six characters
result = [word for word in standardized_words if len(word) > 6]

print(result)
