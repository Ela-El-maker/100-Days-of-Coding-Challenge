

def printHeader():
    print('----------------------------------------------------------')
    print('----------------Guess That Number Game--------------------')
    print('----------------------------------------------------------')
    print()

def runEventLoop():
    print("What do you want to do with your journal :- ")
    cmd = None
    journal_data = [] #list of journal entries
    while cmd != 'X':
        cmd = input("Enter your command [L]ist entries, [A]dd entry, [E]xit: ")
        cmd = cmd.lower().strip()
        if cmd == 'L':
            listEntries(journal_data)
        elif cmd == 'A':
            addEntry(journal_data)
        elif cmd != 'X':
            print("Sorry , we dont understand '{}'.".format(cmd))

    print('Done... Goodbye!')


def listEntries(data):
    if data:
        print('Listing Entries')
        for index, entry in enumerate(data, 1):
            print(f"{index}. {entry}")
    else:
        print('No entries found')

def addEntry(data):
    print('Adding Entry')
    text = input('Type your entry. <Enter> to exit:- ')
    if data:
        data.append(text)
    else:
        print("Empty entry discarded.")

def main():
    printHeader()
    runEventLoop()

main()