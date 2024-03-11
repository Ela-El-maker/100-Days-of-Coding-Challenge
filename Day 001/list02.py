text = 'Python programming'

text = text.lower()

text = text.replace(' ', '')
text = sorted(set(text))

print(text)