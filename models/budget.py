class Budget:
    def __init__(self, total_budget, periodicity, budget_status = None, id = None):
        self.total_budget = total_budget
        self.periodicity = periodicity
        self.budget_status = budget_status
        self.id = id

    def get_total_budget(self):
        return self.total_budget

    def get_budget_periodicity(self):
        return self.periodicity
    
    def get_budget_id(self):
        return self.id
    
    def get_budget_status(self, total_expenses):
        budget_status = self.total_budget - total_expenses
        return budget_status
    
    def budget_alert(self, budget_status):
        if budget_status > 10:
            return f'Your budget is {budget_status}'
        elif budget_status < 10 and budget_status > 0:
            return f'Your budget is {budget_status} and you are running out of money'
        elif budget_status == 0:
            return f'Your budget is {budget_status}, you have run out of money'
        else:
            return f'Your budget is {budget_status}, you are overspending'
