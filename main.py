
def login():
    isAuthenticated = False
    while not isAuthenticated:
        print("Input a username")
        username = input()
        print("Input a password")
        password = input()
        isAuthenticated = authenticate(username, password)
        if isAuthenticated == False:
            print("Invalid username or password")

def signUp():
    createdAccount = False
    while not createdAccount:
        print("Input a username")
        username = input()
        print("Input a password")
        password = input()
        createdAccount = createAccount(username, password)
        if createdAccount == False:
            print("Username is already taken")

def authenticate(username, password):
    return True

def createAccount(username, password):
    return False

mainPageChoices = {1: login, 2: signUp}

def mainPage():
    choice = 0

    while choice not in mainPageChoices:
        print("Please select an option.")
        print("Enter 1 to log in.")
        print("Enter 2 to sign up.")
        userInput = input()
        if userInput.isdigit():
            choice = int(userInput)
        else:
            print("Please enter a number.")
            continue
        if choice in mainPageChoices:
            mainPageChoices[choice]()


if __name__ == '__main__':
    mainPage()
