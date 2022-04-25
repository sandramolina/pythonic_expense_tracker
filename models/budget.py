class Budget:
    def __init__(self, total_budget, periodicity, balance = None, id = None):
        self.total_budget = total_budget
        self.periodicity = periodicity
        self.balance = balance
        self.id = id

    def get_total_budget(self):
        return self.total_budget

    def get_budget_periodicity(self):
        return self.periodicity
    
    def get_budget_id(self):
        return self.id
    
    def get_balance(self, total_expenses):
        balance = self.total_budget - total_expenses
        return balance
    
    def budget_alert(self, balance):
        if balance > 10:
            return f'Your budget is {balance}'
        elif balance < 10 and balance > 0:
            return f'Your budget is {balance} and you are running out of money'
        elif balance == 0:
            return f'Your budget is {balance}, you have run out of money'
        else:
            return f'Your budget is {balance}, you are overspending'
