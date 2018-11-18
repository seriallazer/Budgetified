class Transaction:
    def expense(self, date, desc, transaction_value, origin):
        self.date = date
        self.desc = desc
        self.transaction_value = transaction_value
        self.category = category
        self.origin = origin

    def transfer(self, date, desc, transaction_value, origin, balance):
        expense(self, date, desc, transaction_value, origin)
        self.balance = balance

