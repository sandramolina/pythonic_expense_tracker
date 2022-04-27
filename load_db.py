from models.category import *
import repositories.category_repository as category_repository

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.expense import Expense
import repositories.expense_repository as expense_repository

from models.budget import Budget
import repositories.budget_repository as budget_repository 

#Creating basic DB:
category1 = Category("Groceries")
category_repository.save(category1)

category2 = Category("Transportation")
category_repository.save(category2)

category3 = Category("Gifts")
category_repository.save(category3)

category4 = Category("Armor")
category_repository.save(category4)

category5 = Category("Vengeance")
category_repository.save(category5)

merchant1 = Merchant("The Spice King")
merchant_repository.save(merchant1)

merchant2 = Merchant("Illyrio Mopatis")
merchant_repository.save(merchant2)

merchant3 = Merchant("Yunkai Transport Inc.")
merchant_repository.save(merchant3)

merchant4 = Merchant("Kraznys mo Nakloz")
merchant_repository.save(merchant4)

merchant5 = Merchant("Dragonstone Beauty")
merchant_repository.save(merchant5)

expense1 = Expense("2022-04-25", merchant1, category1, 120, "Dinner with Khal Drogo")
expense_repository.save(expense1)

expense2 = Expense("2020-03-15", merchant3, category2, 49, "Wedding at the Twins")
expense_repository.save(expense2)

expense3 = Expense("2021-01-05", merchant4, category5, 2000, "Getting some new warriors")
expense_repository.save(expense3)

expense4 = Expense("2022-02-28", merchant2, category4, 50000, "Golden helmet")
expense_repository.save(expense4)

expense5 = Expense("2021-02-28", merchant2, category3, 20000, "Present for Jon Snow (Longclaw)")
expense_repository.save(expense5)

expense6 = Expense("2021-02-25", merchant4, category5, 100, "1 bottle of Tears of Lys")
expense_repository.save(expense6)

expense7 = Expense("2021-05-25", merchant1, category1, 80, "Pet food for Viserion")
expense_repository.save(expense7)

expense8 = Expense("2021-06-25", merchant5, category1, 75, "Silver hair dye")
expense_repository.save(expense8)

budget = Budget(100000, "Yearly")
budget_repository.save(budget)
#----------------------------------------------------

# # test select all 
# # print(category_repository.select_all()[1].__dict__)

# # test select
# # print(category_repository.select(2).__dict__)

# # test delete
# # category_repository.delete(2)

# # Testing save function
# merchant1 = Merchant("The Spice King")
# merchant_repository.save(merchant1)

# merchant2 = Merchant("Illyrio Mopatis")
# merchant_repository.save(merchant2)

# merchant3 = Merchant("Yunkai Transport Inc.")
# merchant_repository.save(merchant3)

# merchant4 = Merchant("Kraznys mo Nakloz")
# merchant_repository.save(merchant4)

# # test select all 
# # print(merchant_repository.select_all())

# # test delete
# # merchant_repository.delete(2)

# # Testing save function
# expense1 = Expense("2022-04-25", merchant1, category1, 120, "Dinner with Khal Drogo")
# expense_repository.save(expense1)

# expense2 = Expense("2020-03-15", merchant3, category2, 50, "Wedding at the Twins")
# expense_repository.save(expense2)

# expense3 = Expense("2021-01-05", merchant4, category5, 2000, "Getting some new warriors")
# expense_repository.save(expense3)

# expense4 = Expense("2022-02-28", merchant2, category4, 50000, "Golden helmet")
# expense_repository.save(expense4)

# expense5 = Expense("2021-02-28", merchant2, category3, 20000, "Present for John S. (Longclaw)")
# expense_repository.save(expense5)

# expense6 = Expense("2021-02-25", merchant4, category5, 100, "1 bottle of Tears of Lys")
# expense_repository.save(expense6)

#test select all 
#print(expense_repository.select_all()[0].__dict__)

#print(expense_repository.select(1).__dict__)

#expense_repository.delete_all()

#test get_total_expenses():
#print(expense_repository.get_total_expenses())

#test filter_expenses by merchant
# test = expense_repository.filter_expenses(merchant2)
# print(test[0].__dict__)
# print(test[1].__dict__)

# test = expense_repository.get_subtotal_expenses_by_merchant(merchant4)
# print(test)

# test = expense_repository.get_subtotal_expenses_by_category(category5)
# print(test)

# budget = Budget(10000, "Yearly")
# budget_repository.save(budget)

#print(budget_repository.select_all()[0].__dict__)
#print(budget_repository.select(2).__dict__)

# budget2 = Budget(5000, "Monthly")
# budget_repository.save(budget2)

#budget_repository.delete(3)
# budget.periodicity = "daily"
# budget_repository.update(budget)

#print(budget_repository.balance())

#print(budget_repository.alert())