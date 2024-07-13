class BudgetCategory():
    def __init__(self, name, allocated_budget):
        self.name = name
        self.allocated_budget = allocated_budget

    def get_budget(self):
        return self.allocated_budget
    
    def set_budget(self, new_budget):
        self.allocated_budget = new_budget

    def add_expense(self):
        amount = int(input("How much would you like to add to your budget? "))
        self.set_budget(self.get_budget() + amount)
        print(f"{amount} has been added to your budget successfully. Your new budget is {self.get_budget()}")

    def subtract_from_budget(self):
        amount = int(input("How much would you like to subtract from your budget? "))
        self.set_budget(self.get_budget() - amount)
        print(f"{amount} has been subtracted from your budget successfully. Your new budget is {self.get_budget()}")

    def display_category_summary(self):
        print(f"{self.name}'s allocated budget is {self.allocated_budget}.")

groceries = BudgetCategory("groceries", 400)
print(groceries.add_expense())
print(groceries.display_category_summary())
print(groceries.subtract_from_budget())
