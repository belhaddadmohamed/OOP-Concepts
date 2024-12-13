# Encapsulation
# Definition: Restricts direct access to some of an object's components to protect the integrity of the object.
# Purpose: Prevent unintended interference and allow controlled access to attributes and methods.


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds or invalid amount")

    def get_balance(self):
        return self.__balance


# Usage
account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.owner)  # alice
print(account.get_balance())  # 1500
