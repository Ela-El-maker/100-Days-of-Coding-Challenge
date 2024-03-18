import random


print('----------------------------------------------------------')
print('----------------Guess That Number Game--------------------')
print('----------------------------------------------------------')
print()

theNumber = random.randint(0,100)
guessText = input("Guess a number between 0 and 100 :- ")
guess = int(guessText)

while guess!= theNumber:
    guessText = input("Guess a number between 0 and 100 :- ")
    guess = int(guessText)

    if guess < theNumber:
        print("Your "+guess+" was too low")

    elif guess > theNumber:
        print("Your "+guess+" was too")
    else:
        print("Your "+guess+" was correct")

print("Done!!!")

