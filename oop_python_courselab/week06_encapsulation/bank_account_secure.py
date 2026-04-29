class BankAccount_nbs:
    def __init__(self_nbs, balance_nbs):
        self_nbs.__balance = balance_nbs

    def deposit_nbs(self_nbs, amount_nbs):
        self_nbs.__balance += amount_nbs

    def withdraw_nbs(self_nbs, amount_nbs):
        if amount_nbs <= self_nbs.__balance:
            self_nbs.__balance -= amount_nbs
        else:
            print("Insufficient funds")

    def get_balance_nbs(self_nbs):
        return self_nbs.__balance

account_nbs = BankAccount_nbs(5000)
account_nbs.deposit_nbs(1000)
account_nbs.withdraw_nbs(2000)
print("Balance_nbs:", account_nbs.get_balance_nbs())

#Nicole B. Sambile