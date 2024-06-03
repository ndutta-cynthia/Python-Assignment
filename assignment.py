class Account:
    def __init__(self, number, pin, owner_name, owner_address, owner_phone):
        self.number = number
        self.__pin = pin
        self.__balance = 0
        self.__owner_name = owner_name
        self.__owner_address = owner_address
        self.__owner_phone = owner_phone
        self.__overdraft_limit = 0
        self.__minimum_balance = 0
        self.__transaction_history = []
        self.__frozen = False
    def check_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "Wrong pin"
    def deposit(self, amount, pin):
        if pin == self.__pin:
            self.__balance += amount
            self.__transaction_history.append(f"Deposit: {amount}")
        else:
            return "Wrong pin"
    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if self.__balance - amount >= -self.__overdraft_limit:
                self.__balance -= amount
                self.__transaction_history.append(f"Withdrawal: {amount}")
            else:
                return "Insufficient funds"
        else:
            return "Wrong pin"
    def view_account_details(self, pin):
        if pin == self.__pin:
            return f"Account Number: {self.number}\nOwner Name: {self.__owner_name}\nOwner Address: {self.__owner_address}\nOwner Phone: {self.__owner_phone}\nBalance: {self.__balance}"
        else:
            return "Wrong pin"
    def change_owner_details(self, pin, new_name, new_address, new_phone):
        if pin == self.__pin:
            self.__owner_name = new_name
            self.__owner_address = new_address
            self.__owner_phone = new_phone
        else:
            return "Wrong pin"
    def account_statement(self, pin):
        if pin == self.__pin:
            return "\n".join(self.__transaction_history)
        else:
            return "Wrong pin"
    def set_overdraft_limit(self, pin, limit):
        if pin == self.__pin:
            self.__overdraft_limit = limit
        else:
            return "Wrong pin"
    def calculate_interest(self, pin, rate):
        if pin == self.__pin:
            interest = self.__balance * rate
            self.__balance += interest
            self.__transaction_history.append(f"Interest: {interest}")
        else:
            return "Wrong pin"
    def freeze_account(self, pin):
        if pin == self.__pin:
            self.__frozen = True
        else:
            return "Wrong pin"
    def unfreeze_account(self, pin):
        if pin == self.__pin:
            self.__frozen = False
        else:
            return "Wrong pin"
    def set_minimum_balance(self, pin, minimum_balance):
        if pin == self.__pin:
            self.__minimum_balance = minimum_balance
        else:
            return "Wrong pin"
    def transfer_funds(self, pin, recipient_account, amount):
        if pin == self.__pin:
            if self.__balance - amount >= -self.__overdraft_limit:
                self.__balance -= amount
                recipient_account.__balance += amount
                self.__transaction_history.append(f"Transfer to {recipient_account.number}: {amount}")
                recipient_account.__transaction_history.append(f"Transfer from {self.number}: {amount}")
            else:
                return "Insufficient funds"
        else:
            return "Wrong pin"
    def close_account(self, pin):
        if pin == self.__pin:
            if self.__balance == 0:
                return "Account closed successfully"
            else:
                return "Cannot close account with non-zero balance"
        else:
            return "Wrong pin"