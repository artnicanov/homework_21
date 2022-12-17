from base_storage import BaseStorage
from errors_and_exeption import UniqueNamesError

class Shop(BaseStorage):
	def __init__(self, items, capacity: int=20):
		super().__init__(items, capacity)  # используются методы родительского класса

	def add(self, name: str, qnt: int):
		if self.get_unique_items_count() >= 5:
			raise UniqueNamesError
		super().add(name, qnt)  # используются методы родительского класса