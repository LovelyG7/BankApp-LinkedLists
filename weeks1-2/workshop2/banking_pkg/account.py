def show_balance(balance):
    print(float(balance))


def deposit(balance):
    amount = input("Enter amount to deposit: ")
    balance = float(balance) + float(amount)
    return balance


def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    balance = float(balance) - float(amount)
    return balance


def logout(name):
    print("Goodbye, ", name, "!")
