from base_storage import BaseStorage

class Store(BaseStorage):
	def __init__(self, items, capacity: int=100):
		super().__init__(items, capacity)  # используются методы родительского класса