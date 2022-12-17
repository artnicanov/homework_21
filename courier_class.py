from storage_class import Storage
from request_class import Request

class Courier():
	def __init__(self, request, storages):
		self.__request = request
		self.__from = storages[self.__request.source]
		self.__to = storages[self.__request.destination]

	def delivery_action(self):
		self.__from.remove(name=self.__request.product, qnt=self.__request.amount)
		print(f"Курьер забирает {self.__request.amount} {self.__request.product} из {self.__request.source}")
		print(f"Курьер везет {self.__request.amount} {self.__request.product} из {self.__request.source} в {self.__request.destination}")
		print(f"Курьер доставил {self.__request.amount} {self.__request.product} в {self.__request.destination}")

		self.__to.add(name=self.__request.product, qnt=self.__request.amount)


