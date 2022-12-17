class BaseError(Exception):
	message = "в программе ошибка"

class CapacityError(BaseError):
	message = "Недостаточно места"

class NameError(BaseError):
	message = "Неизвестный товар"

class AmountError(BaseError):
	message = "Недостаточно товара"

class RequestError(BaseError):
	message = "Неверный запрос"

class StorageNameError(BaseError):
	message = "Неизвестное место хранения"

class UniqueNamesError(BaseError):
	message = "Нельзя хранить в магазине более 5 уникальных товаров"