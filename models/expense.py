class Expense:
    def __init__(self, date, merchant, category, amount, description, id = None):
        self.date = date
        self.merchant = merchant
        self.category = category
        self.amount = amount
        self.description = description
        self.id = id