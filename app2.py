DB = {"Emmanuel":"1234a", "Sam":"4321a", "Tom":"1212a"}  

def signup():
    while True:
        newUser = input("Please create a unique userName: ")
        if newUser in DB:
            print("Username", newUser, "is already in use. Please try another.")
        else:
            newPassword = input("Enter you prefered password.")
            DB[newUser] = newPassword
            print("You have successfully signed up as:", newUser)
            print(DB)
            break

def login():
    userName = input("Enter your username: ")
    password = input("enter your password: ")
    if userName in DB and password == DB[userName]:
        print("welcome")
    else:
        print("User not found!\nkindly create a new account")
        Begin()

def Begin():
    try:
        Selection = int(input(
            "Hello there, welcome!\n"
            "What do you want to do:\n"
            "For Login press 1\n"
            "For Signup press 2\n"
        ))

        if Selection == 1:
            login()
        elif Selection == 2:
            signup()
        else:
            print("Invalid selection.")
            Begin()
    except ValueError:
        print("Please enter a valid number.")
        Begin()

Begin()