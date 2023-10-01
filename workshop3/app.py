from donations_pkg import user
from donations_pkg import homepage

database = {"admin": "password123"}
donations = []
authorized_user = ""


if authorized_user == "":
    print("You must be logged in to donate")
else:
    print("Logged in as: ", authorized_user)

# Handle user input
while True:
    homepage.show_homepage()
    user_input = int(input("Choose an option: "))
    if user_input == 1:
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        authorized_user = user.login(database, username, password)
    elif user_input == 2:
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        authorized_user = user.register(database, username)
        if authorized_user != "":
            database[username] = password
            # print(database.keys())
    elif user_input == 3:
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_string = homepage.donate(authorized_user)
            donations.append(donation_string)
    elif user_input == 4:
        homepage.show_donations(donations)
    elif user_input == 5:
        print("Leaving DonateMe...")
        break
    else:
        print("Please choose a valid option")
