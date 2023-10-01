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

user1 = User("jane", "jane@nucamp.co", "janespassword")
print(user1.password)
user1.change_password("bestpassword")

