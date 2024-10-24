
def createCollection():
    print("Create collection")
    homePage()

def deleteCollection():
    print("Delete collection")
    homePage()

def renameCollection():
    print("Rename collection")
    homePage()

def listCollection():
    print("List collection")
    homePage()

def searchVideoGame():
    print("Search video game")
    homePage()

def followUser():
    print("Follow user")
    homePage()

def unfollowUser():
    print("Unfollow user")
    homePage()

def whoYouFollow():
    print("Who you follow")
    homePage()

def logOut():
    print("Log out")
    mainPage()

homePageChoices= {1: createCollection, 2: deleteCollection, 3: renameCollection, 4: listCollection, 5: searchVideoGame, 6: followUser, 7: unfollowUser, 8: whoYouFollow, 9: logOut}

def homePage():
    choice = 0

    while choice not in homePageChoices:
        print("Welcome to the home page")
        print("Please choose an option by selecting a number")
        print("Collection Operations")
        print("1. Create Collection")
        print("2. Delete Collection")
        print("3. Rename Collection")
        print("4. List Collections")
        print("Video games operations")
        print("5. Search for Video games")
        print("Social Operations")
        print("6. Follow user")
        print("7. Unfollow user")
        print("8. See who you follow")
        print("9. Logout")
        userInput = input()
        if userInput.isdigit():
            choice = int(userInput)
        else:
            print("Please enter a number.")
            continue
        if choice in homePageChoices:
            homePageChoices[choice]()


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
        print("Succesfully logged in")
        print("")
        homePage()


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
        print("Account Created!")
        print("")
        mainPage()
def authenticate(username, password):
    return True

def createAccount(username, password):
    return True

mainPageChoices = {1: login, 2: signUp}

def mainPage():
    choice = 0

    while choice not in mainPageChoices:
        print("Please select an option.")
        print("Enter 1 to log in.")
        print("Enter 2 to sign up.")
        print("Enter 3 to terminate Program.")
        userInput = input()
        if userInput.isdigit():
            choice = int(userInput)
        else:
            print("Please enter a number.")
            continue
        if choice in mainPageChoices:
            mainPageChoices[choice]()
        if choice == 3:
            return


if __name__ == '__main__':
    mainPage()
