import datetime

print('----------------------------------------------------------')
print('----------------Guess That Number Game--------------------')
print('----------------------------------------------------------')
print()

def getBirthday():
    print('Tell us when you were born:- ')
    year = int(input('Year [YYYY] :- '))
    month = int(input('Month [MM] :- '))
    day = int(input('Day [DD] :- '))

    birthday = datetime.datetime(year, month, day)
    return birthday

def computeDates(originalDate):
    now = datetime.datetime.now()
    date1 = now
    date2 = datetime.datetime(now.year, originalDate.month, originalDate.day)
    dt = date2 - date1
    days = dt.days
    return days

def displayInfo(days):
    if days < 0:
        print('Your birthday is in {} days'.format(-days))
    elif days > 0:
        print("You had your birthday already {} days ago!".format(days))
    else:
        print("Your birthday is today!")

def main():
    bday = getBirthday()
    print(bday)
    numberOfDays = computeDates(bday)
    displayInfo(numberOfDays)

main()
