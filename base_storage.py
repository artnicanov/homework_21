from storage_class import Storage
from errors_and_exeption import CapacityError, NameError, AmountError

class BaseStorage(Storage):
	def __init__(self, items, capacity):
		""" конструктор класса принимает поля:
		 items (словарь название:количество)
		capacity (целое число)"""
		self._items = items
		self._capacity = capacity  # защищенное поле из-за нижнего подчеркивания

	def add(self, name: str, qnt: int):
		""" увеличивает запас items на величину количества qnt"""
		if self.get_free_space() < qnt:
			# покажем ошибку если нет места на складе
			raise CapacityError

		if name in self._items:
			# выполняем условие в зависимости от наличия такого названия
			self._items[name] += qnt
		else:
			self._items[name] = qnt

	def remove(self, name: str, qnt: int):
		"""уменьшает запас item"""
		if name not in self._items:
			# покажем ошибку если нет такого товара
			raise NameError

		if self._items[name] < qnt:
			# покажем ошибку если товара недостаточно
			raise AmountError

		self._items[name] -= qnt

	def get_free_space(self):
		"""из всего объема склада вычитаем сумму значений в словаре items"""
		return self._capacity - sum(self._items.values())

	def get_items(self):
		"""возвращает содержание склада в словаре {товар: количество}"""
		return self._items

	def get_unique_items_count(self):
		""" возвращает длину словаря, т.е. количество уникальных ключей"""
		return len(self._items)