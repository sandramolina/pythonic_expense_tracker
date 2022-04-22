from models.category import *
import repositories.category_repository as category_repository

#Testing save function
category1 = Category("Groceries")
category_repository.save(category1)
