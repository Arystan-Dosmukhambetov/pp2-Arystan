class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            return self.balance


# Input
initial_balance, withdraw_amount = map(int, input().split())

# Create account (owner can be anything, not required in output)
acc = Account("User", initial_balance)

# Withdraw and print result
result = acc.withdraw(withdraw_amount)
print(result)
