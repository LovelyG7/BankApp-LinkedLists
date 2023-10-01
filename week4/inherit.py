class User:
    def __init__(self, name, email, password): 
        self.name = name
        self.email = email
        self.password = password
   
   # How to define an instance method in a class
   #Make a method to change the password by defining inside the class
    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)

class BankUser(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0

    def check_balance(self):
        print(self,name, "has an account balance of:",self.balance)

bankuser1 = BankUser("Jane","jane@nucamp.co","bestpassword")
