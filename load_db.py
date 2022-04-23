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

category3 = Category("Gifts")
category_repository.save(category3)

category4 = Category("Armor")
category_repository.save(category4)

category5 = Category("Vengeance")
category_repository.save(category5)

#test select all 
#print(category_repository.select_all()[1].__dict__)

#test select
#print(category_repository.select(2).__dict__)

#test delete
#category_repository.delete(2)

#Testing save function
merchant1 = Merchant("The Spice King")
merchant_repository.save(merchant1)

merchant2 = Merchant("Illyrio Mopatis")
merchant_repository.save(merchant2)

merchant3 = Merchant("Yunkai Transport Inc.")
merchant_repository.save(merchant3)

merchant4 = Merchant("Kraznys mo Nakloz")
merchant_repository.save(merchant4)
#test select all 
#print(merchant_repository.select_all())

#test delete
#merchant_repository.delete(2)

#Testing save function
expense1 = Expense("2022-04-25", merchant1, category1, 120, "Dinner with Khal Drogo")
expense_repository.save(expense1)

expense2 = Expense("2020-03-15", merchant3, category2, 50, "Wedding at the Twins")
expense_repository.save(expense2)

expense3 = Expense("2021-01-05", merchant4, category5, 2000, "Getting some new warriors")
expense_repository.save(expense3)

expense4 = Expense("2022-02-28", merchant2, category4, 50000, "Golden helmet")
expense_repository.save(expense4)

expense5 = Expense("2021-02-28", merchant2, category3, 20000, "Present for John S. (Longclaw)")
expense_repository.save(expense5)

expense6 = Expense("2021-02-25", merchant4, category5, 100, "1 bottle of Tears of Lys")
expense_repository.save(expense3)

#test select all 
#print(expense_repository.select_all()[0].__dict__)

#print(expense_repository.select(1).__dict__)

#expense_repository.delete_all()

#test get_total_expenses():
#print(expense_repository.get_total_expenses())