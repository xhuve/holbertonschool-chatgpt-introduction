class Checkbook:
    """
    A simple checkbook class that allows deposits, withdrawals, and checking the balance.
    """

    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                print("Invalid amount. Amount must be a positive number.")
            else:
                self.balance += amount
                print("Deposited ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                print("Invalid amount. Amount must be a positive number.")
            elif amount > self.balance:
                print("Insufficient funds to complete the withdrawal.")
            else:
                self.balance -= amount
                print("Withdrew ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            amount = input("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = input("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
