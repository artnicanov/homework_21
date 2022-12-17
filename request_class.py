from storage_class import Storage
from errors_and_exeption import RequestError, StorageNameError

class Request:
	def __init__(self, request, storages):
		"""При инициализации  принимает список всех складов и строку типа
		Доставить 3 печеньки из склад в магазин"""

		request_split = request.lower().split(' ')  # делим строку запроса по пробелу, чтобы достать нужные параметры
		if len(request_split) != 7:
			# покажем ошибку если запрос не по шаблону
			raise RequestError

		self.amount = int(request_split[1])
		self.product = request_split[2]
		self.source = request_split[4]
		self.destination = request_split[6]

		if self.source not in storages or self.destination not in storages:
			# покажем ошибку если указано неизвесттное место хранения
			raise StorageNameError