class BankAccount:
    def __init__(self, owner_name, account_number, balance=0.0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сума для поповнення повинна бути більше нуля.")
        self.balance += amount
        print(f"Рахунок {self.account_number} поповнено на {amount:.2f}. Новий баланс: {self.balance:.2f}.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сума для зняття повинна бути більше нуля.")
        if amount > self.balance:
            raise ValueError("Недостатньо коштів на рахунку.")
        self.balance -= amount
        print(f"З рахунку {self.account_number} знято {amount:.2f}. Новий баланс: {self.balance:.2f}.")

    def __str__(self):
        return f"Власник: {self.owner_name}, Номер рахунку: {self.account_number}, Баланс: {self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        if account.account_number in self.accounts:
            raise ValueError("Рахунок з таким номером вже існує.")
        self.accounts[account.account_number] = account
        print(f"Рахунок {account.account_number} додано.")

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number not in self.accounts or to_account_number not in self.accounts:
            raise ValueError("Один або обидва рахунки не знайдено.")
        from_account = self.accounts[from_account_number]
        to_account = self.accounts[to_account_number]

        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f"Переказано {amount:.2f} з рахунку {from_account_number} на рахунок {to_account_number}.")

    def get_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Рахунок не знайдено.")
        return self.accounts[account_number]

if __name__ == "__main__":

    bank = Bank()

    account1 = BankAccount("Іван Карась", "123456", 1000)
    account2 = BankAccount("Марія Жовтень", "654321", 500)

    bank.add_account(account1)
    bank.add_account(account2)

    account1.deposit(500)

    account2.withdraw(200)

    bank.transfer("123456", "654321", 300)

    print(account1)
    print(account2)
