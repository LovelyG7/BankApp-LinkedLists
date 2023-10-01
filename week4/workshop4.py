

# Task One
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

# Task Two
    def change_name(self, name):
        print("Your name has been changed to", self.name)

    def change_pin(self, pin):
        print("Your pin has been changed to", self.pin)

    def change_password(self, password):
        print("Your password has been changed to", self.password)

# Task Three


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

# Task Four
    def show_balance(self):
        print(self.name, "has a balance of ", self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

# Task Five
    def transfer(self, amount, user):
        print(self.name, "is transferring", amount, "to", user.name)
        pin_veri = int(input("Enter your pin: "))
        if self.pin == pin_veri:
            print("you have been verified")
        else:
            print("Invalid Pin")
            return False
        self.balance -= amount
        user.balance += amount

    def request_money(self, amount, user):
        print(user.name, "is Requesting", amount, "from", self.name)
        pin_verify = int(input("Enter your PIN: "))
        password_verify = input("Enter your Password: ")
        if user.pin == pin_verify:
            print("You have been verified")
        else:
            print("Invalid PIN. Transaction canceled")
            return False
        if user.password == password_verify:
            print("Request Authorized")
        else:
            print("Invalid Password")
            return False
        user.balance -= amount
        self.balance += amount


"""
            ---------- Task One ----------
    - Declare a class and give it the name "User"
    - The __init__ method has parameters defined as
      (self, name, pin, password)
    - The attribute of the User class are defined as
       name, pin, and password
"""
""" Driver Code for Task One """
User1 = User("Bob", 1234, "password")

''' Output: Bob 1234 password '''
print(User1.name, User1.pin, User1.password)

"""
            ---------- Task Two ----------
    The "User" class should have three methods:
        * change_name - changes the name of User
        * change_pin - changes the PIN code of User
        * change_password - changes the password of User
    """
""" Driver Code for Task Two """
User1.change_name("Bobby")
User1.change_pin(456)
User1.change_password("tree")

''' Output: Bobby 456 tree '''
print(User1.name, User1.pin, User1.password)

"""
            ---------- Task Three ----------
    tre- Declare a class and give it the name "BankUser"
    - "BankUser" class will inherit the "User" class
    - The __init__ method has parameters defined as
      (self, name, pin, password)
    - The super method has parameters defined as
      (name, pin, password)
    - The attributes of the "BankUser" is balance with
      a default value of zero.
"""
BankUser1 = BankUser("Sarah", 1234, "password")

# """
#             ----------Task Four ----------
# The "BankUser" class should have three methods:
# * show_balance- prints the balance of the User
# * withdraw - withdrawing money decreases the account balance
# * deposit - depositing money increases the account balance
# """
BankUser2 = BankUser("Tom", 456, "tree")
BankUser1 = BankUser("Sarah", 1234, "password")
BankUser2.show_balance()
BankUser2.deposit(5000)
BankUser2.show_balance()
BankUser1.withdraw(10)
BankUser1.show_balance()
# """
#             ----------Task Five ----------
# Create two more methods for the BankUser class:
#  * transfer_money
#   - Transfers money to another User if
#   - correct PIN is given for transferring User
# * request_money
# - Will ask for the PIN of the User being requested for money.
# - If credentials are correct,
#  - Will ask for and validate the password of the User requesting money as well,
#  - Then complete the transfer, removing money from one account and adding the same amount to the other.
#     """
BankUser2.transfer(500, BankUser1)
BankUser2.show_balance()
BankUser1.show_balance()

BankUser1.request_money(250, BankUser2)
BankUser2.show_balance()
BankUser1.show_balance()

# """ Driver Code for Task One """

# ''' Output: Bob 1234 password '''

# """ Driver Code for Task Two """

# ''' Output: Bobby 4321 newpassword '''

# """ Driver Code for Task Three """

# ''' Output: Bob 1234 password 0'''

# """ Driver Code for Task Four """

# ''' Output:
#         Alice has an account balance of: 0
#         Alice has an account balance of: 1000.0
#         Alice has an account balance of: 500.0
# '''

# """ Driver Code for Task Five """

# ''' Output:
#         Alice has an account balance of: 5000
#         Bob has an account balance of: 0
# ​
#         You are transferring $500 to Bob
#         Authentication required
#         Enter your PIN: 5678
#         Transfer authorized
#         Transferring $500 to Bob
#         Alice has an account balance of: 4500
#         Bob has an account balance of: 500
# ​
#         You are requesting $250 from Bob
#         User authentication is required...
#         Enter Bob's PIN: 1234
#         Enter your password: alicepassword
#         Request authorized
#         Bob sent $250
#         Alice has an account balance of: 4750
#         Bob has an account balance of: 250
# '''
