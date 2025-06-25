DB = ["Emmanuel", "Sam", "Tom"]  

def signup():
    while True:
        newUser = input("Please create a unique username: ")
        if newUser in DB:
            print("Username", newUser, "is already in use. Please try another.")
        else:
            DB.append(newUser)
            print("You have successfully signed up as:", newUser)
            print(DB)
            break

def login():
    username = input("Enter your username: ")
    if username in DB:
        print("Welcome", username)
    else:
        print("User not found!")
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