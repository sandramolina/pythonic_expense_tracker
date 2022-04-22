from models.category import *
import repositories.category_repository as category_repository

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

#Testing save function
# category1 = Category("Groceries")
# category_repository.save(category1)

# category2 = Category("Transportation")
# category_repository.save(category2)

#test select all 
#print(category_repository.select_all()[1].__dict__)

#test select
#print(category_repository.select(2).__dict__)

#test delete
#category_repository.delete(2)

#Testing save function
# merchant1 = Merchant("Tesco")
# merchant_repository.save(merchant1)

# merchant2 = Merchant("The Pony Inn")
# merchant_repository.save(merchant2)