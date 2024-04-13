	count = 0
    for c in word:
        if c.isupper() is True:
            count += 1
            
    L = len(word)
    if count == L:
        return True
    elif count == 0:
        return True
    elif count == 1 & word[0].isupper():
        return True
    else: return False