import sqlite3

print("1. Log into an Existing account. \n2. Create a account. \n3. Delete an existing account.")
user_choice = int(input("->"))

db = sqlite3.connect("ui.sqlite") # You can change the name of the tabel before you run it from ui to whatever you want. 
cursor = db.cursor()              # MAKE SURE YOU CHANGE ALL INSTANCES OF THE CURRENT NAME OF THE TABLE IN THE CODE 
                                  # (THIS ONLY APPLIES IF YOU WANNA CHANGE THE TABLES NAME!))

db.execute("CREATE TABLE IF NOT EXISTS ui (Username TEXT, Password TEXT)")
db.commit()

if user_choice == 1:

    user1 = input("Enter a Username: ")
    user2 = input("Enter a Password: ")

    print()

    cursor.execute("SELECT Username from ui where Username = '{}' LIMIT 1".format(user1))
    if cursor.fetchone():
        print("Username Success")
        username = True
    else:
        print("Username Fail")
        username = False
    cursor.execute("SELECT Password from ui where Password = '{}' LIMIT 1".format(user2))
    if cursor.fetchone():
        print("Password Success")
        password = True
    else:
        print("Password Fail")
        password = False
    if username == True and password == True:
        print("Login Success")
        print()
    else:
        print("Login Failed")
        print()

elif user_choice == 2:

    user3 = input("Enter your new username: ")
    user4 = input("Enter your new password: ")
    print()

    cursor.execute("SELECT Username from ui where Username = '{}' LIMIT 1".format(user3))
    if cursor.fetchone():
        print("Username Already exists. Try another one.")
        print()
    else:
        print("Username Available")
        cursor.execute("SELECT Password from ui where Password = '{}' LIMIT 1".format(user4))
        if cursor.fetchone():
            print("Oops there was an error enter another Password!")
            print()
        else:
            print("Password Success")
            db.execute("INSERT INTO ui(Username, Password) VALUES('{}', '{}')".format(user3, user4))
            db.commit()
            print()
            print("You have successfully created a new Account!")
            print()


elif user_choice == 3:
    print("In order to delete your account we have to confirm its you. Enter your Username and Password"
          " and your account will be deleted.")
    print()
    user5 = input("Enter your Username: ")
    user6 = input("Enter your Password: ")
    print()

    cursor.execute("SELECT Username from ui where Username = '{}' LIMIT 1".format(user5))
    if cursor.fetchone():
        print("Username Success.")
        cursor.execute("SELECT Password from ui where Password = '{}' LIMIT 1".format(user6))
        if cursor.fetchone():
            print("Password Success. \nDeleting Account now")
            db.execute("DELETE FROM ui WHERE Username = '{}'".format(user5))
            db.execute("DELETE FROM ui WHERE Password = '{}'".format(user6))
            db.commit()
            print()
        else:
            print("Password does not exist or was entered incorrectly.")
            print()
    else:
        print("Username does not exist, or was entered incorrectly.")
        print()

        
# FOR TESTING DELETE THE NEXT 6 LINES AFTER YOU DONE TESTING IT. #
print("SHOWING ALL ACCOUNTS NOW")
cursor.execute("SELECT * FROM ui")
for Username, Password in cursor:
    print(Username)
    print(Password)
    print("-" * 20)
#-----------------------------------------------------------------#
    
cursor.close()
db.close()
