DB = ["Emmanuel"]

def login(Username=input("enter your Username: ")):
    global DB
    if Username not in DB:
        print ("user not found")
        print("Welcome, an account has now been created for you", Username)
        DB.append(Username)
        print(DB)
    else:
        print("Welcome back:", Username)
    print("current users", DB)
login()