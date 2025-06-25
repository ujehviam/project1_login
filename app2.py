import sqlite3
conn = sqlite3.connect('Project1.db') #this creates a database file if it does not already exist
cursor = conn.cursor() 

cursor.execute('''
CREATE TABLE IF NOT EXISTS users_login_credentials (
    userName TEXT PRIMARY KEY,
    PASSWORD TEXT NOT NULL
)
''')

conn.commit()

def signup():
    while True:
        newUser = input("Please create a unique userName: ").capitalize()
        cursor.execute("SELECT * FROM users_login_credentials WHERE userName = ?", (newUser,))
        if cursor.fetchone():
            print("Username", newUser, "is already in use. Please try another.")
        else:
            newPassword = input("Enter you prefered password.")
            cursor.execute("INSERT INTO users_login_credentials (userName, password) VALUES (?, ?)", (newUser, newPassword))
            conn.commit()
            print("You have successfully signed up as:", newUser)
            break

def login():
    userName = input("Enter your username: ").capitalize()
    password = input("enter your password: ")
    cursor.execute("SELECT * FROM users_login_credentials WHERE userName = ? AND password =?", (userName, password))
    if cursor.fetchone():
        print("welcome")
    else:
        print("User not found!\n\n\nkindly create a new account\n")
        Begin()

def Begin():
    try:
        Selection = int(input(
            "Hello there, welcome!\n"
            "What do you want to do:\n"
            "For Login press 1\n"
            "For Signup press 2\n"
            "to exit press 3\n"
        ))

        if Selection == 1:
            login()
        elif Selection == 2:
            signup()
        elif Selection == 3:
            print("goodbye")
            conn.close()
        else:
            print("Invalid selection.\n\n")
            Begin()
    except ValueError:
        print("Please enter a valid number.\n\n")
        Begin()

Begin()