from models.category import *
import repositories.category_repository as category_repository

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.expense import Expense
import repositories.expense_repository as expense_repository

#Testing save function
category1 = Category("Groceries")
category_repository.save(category1)

category2 = Category("Transportation")
category_repository.save(category2)

#test select all 
#print(category_repository.select_all()[1].__dict__)

#test select
#print(category_repository.select(2).__dict__)

#test delete
#category_repository.delete(2)

#Testing save function
merchant1 = Merchant("Tesco")
merchant_repository.save(merchant1)

merchant2 = Merchant("The Pony Inn")
merchant_repository.save(merchant2)

#test select all 
#print(merchant_repository.select_all())

#test delete
#merchant_repository.delete(2)

#Testing save function
expense1 = Expense("2022-04-25", merchant2, category1, 120, "Dinner with Khal Drogo")
expense_repository.save(expense1)

#test select all 
#print(expense_repository.select_all()[0].__dict__)

#print(expense_repository.select(1).__dict__)

#expense_repository.delete_all()