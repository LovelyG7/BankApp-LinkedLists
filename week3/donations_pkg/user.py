def login(database, username, password):
    if username in database.keys() and password == database[username]:
        print("Welcome", username, "!")
        return username
    elif username in database.keys() and password != database[username]:
        print("Incorrect Password")
        return ""
    else:
        print("Username not found")
        return ""


def register(database, username):
    if username in database.keys():
        print("Username already registered.")
        return ""
    else:
        print("Your username has been registered.")
        return username
