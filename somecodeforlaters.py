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


#TEST FOR BUDGET CLASS
#setup:
# self.total_expenses1 = 8000
# self.total_expenses2 = 9999
# self.total_expenses3 = 10000
# self.total_expenses4 = 11000


def test_budget_status(self):
    budget_status = self.budget.budget_status(self.total_expenses1)
    self.assertEqual(2000, budget_status)

def test_budget_alert_over10(self):
    budget_status = self.budget.budget_status(self.total_expenses1)
    alert = self.budget.budget_alert(budget_status)
    self.assertEqual("Your budget is 2000", alert)

def test_budget_alert_minor10(self):
    budget_status = self.budget.budget_status(self.total_expenses2)
    alert = self.budget.budget_alert(budget_status)
    self.assertEqual("Your budget is 1 and you are running out of money", alert)

def test_budget_alert_0(self):
    budget_status = self.budget.budget_status(self.total_expenses3)
    alert = self.budget.budget_alert(budget_status)
    self.assertEqual("Your budget is 0, you have run out of money", alert)

def test_budget_alert_negative(self):
    budget_status = self.budget.budget_status(self.total_expenses4)
    alert = self.budget.budget_alert(budget_status)
    self.assertEqual("Your budget is -1000, you are overspending", alert)