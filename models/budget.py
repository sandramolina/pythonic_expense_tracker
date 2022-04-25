class Budget:
    def __init__(self, total_budget, periodicity, id = None):
        self.total_budget = total_budget
        self.periodicity = periodicity
        self.id = id

    def get_total_budget(self):
        return self.total_budget

    def get_budget_periodicity(self):
        return self.periodicity
    
    def get_budget_id(self):
        return self.id
