import sqlite3
conn = sqlite3.connect('Project1.db') #this creates a database file if it does not already exist
cursor = conn.cursor() 

cursor.execute('''
CREATE TABLE IF NOT EXISTS users_login_credentials (
    userName TEXT PRIMARY KEY NOT NULL,
    password TEXT NOT NULL
)
''') # creats a table

conn.commit() #saving all the modifications

def signup():
    while True:
        newUser = input("Please create a unique userName: ").capitalize()
        cursor.execute("SELECT * FROM users_login_credentials WHERE userName = ?", (newUser,))
        if cursor.fetchone(): #from the single row requested above, check if the username matches
            print("Username", newUser, "is already in use. Please try another.")
        else:
            createPassword = input("Enter you prefered password.")
            cursor.execute("INSERT INTO users_login_credentials (userName, password) VALUES (?, ?)", (newUser, createPassword))#creates a new row and insert the usernam and password
            conn.commit() #save all modifications done on the table
            print("You have successfully signed up as:", newUser)
            break

def login():
    userName = input("Enter your username: ").capitalize()
    password = input("enter your password: ")
    cursor.execute("SELECT * FROM users_login_credentials WHERE userName = ? AND password =?", (userName, password))#query the table for the username
    if cursor.fetchone():#check if username exist in the table
        print("welcome")
    else:
        print("User not found!\n\n\nkindly create a new account\n")
        Begin()

def password_reset():
    userName = input("Enter your username:\n ").capitalize()
    cursor.execute("SELECT * FROM users_login_credentials WHERE userName = ?",(userName,))
    if cursor.fetchone() is None:
        print("kindly enter a valid username or signup\n\n")
        Begin()
    else:
        newPassword1 = input("enter your new password: ")
        newPassword2 = input("enter your new password again: ")

        if newPassword1 == newPassword2:
            cursor.execute("UPDATE users_login_credentials SET PASSWORD = ? WHERE userName = ?", (newPassword1, userName))
            print("\n PASSWORD HAS BEEN SUCCESSFULLY CHANGED \n")
            conn.commit()
        else:
            print("\n PASSWORD DOES NOT MATCH!\n")
            password_reset()    

def Begin():
    try:
        Selection = int(input(
            "Hello there, welcome!\n"
            "What do you want to do:\n"
            "For Login press 1\n"
            "For Signup press 2\n"
            "for password reset 3\n"
            "to exit press 4\n"
        ))

        if Selection == 1:
            login()
        elif Selection == 2:
            signup()
        elif Selection == 3:
            password_reset()
        elif Selection == 4:
            print("goodbye")
            conn.close()#stop and close connection to the database.
        else:
            print("Invalid selection.\n\n")
            Begin()
    except ValueError:
        print("Please enter a valid number.\n\n")
        Begin()

Begin()