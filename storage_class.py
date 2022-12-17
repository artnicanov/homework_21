from abc import ABC, abstractmethod

class Storage(ABC):
	""" это абстрактный класс склада,
	 некий условный шаблон для других классов-наследников """

	@abstractmethod
	def add(self, name: str, qnt: int):
		"""увеличивает запас items"""
		pass

	@abstractmethod
	def remove(self, name: str, qnt: int):
		"""уменьшает запас item"""
		pass

	@abstractmethod
	def get_free_space(self):
		"""вернуть количество свободных мест"""
		pass
	@abstractmethod
	def get_items(self):
		"""возвращает содержание склада в словаре {товар: количество}"""
		pass

	@abstractmethod
	def get_unique_items_count(self):
		"""возвращает количество уникальных товаров"""
		pass
