class Positive:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name
    
    def __get__ (self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Balance Cannot be negative !!")
        setattr(instance, self.private_name, value)

class BankAccount:
    balance = Positive()

    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.balance = initial_balance
    
    def __repr__(self):
        return f"Bank Account Owner: {self.owner}, Balance: {self.balance}"

acc1 = BankAccount("Osama", 122)
print(acc1)

acc1.balance = 300
print(acc1)

acc1.balance = -500
print(acc1)


# acc2 = BankAccount("Ahmed", -200)
# print(acc2)

