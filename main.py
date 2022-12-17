from shop_class import Shop
from store_class import Store
from request_class import Request
from courier_class import Courier
from errors_and_exeption import BaseError

# магазин
shop = Shop(
	items={
		"товар1": 13,
		"товар2": 14,
		"товар3": 14,
		"товар4": 14,
		"товар5": 14,
	}
)

# склад
store = Store(
	items={
		"товар1": 15,
		"товар2": 14,
		"товар6": 14,
	}
)

# в этом слолваре храним все возможные места хранениния
storages = {
	"магазин": shop,
	"склад": store
}

def main():
	# выводим содержимое складов
	while True:
		for storage_name in storages:
			print(f"В {storage_name} хранится {storages[storage_name].get_items()}")

		# запрашиваем у пользователя что нужно доставить, в каком количестве и куда
		user_input = input("Что нужно доставить и куда?\n"
		                   "В формате\n"
		                   "Доставить <количество> <товар> из <место хранения> в <новое место хранения>\n")

		if user_input.lower() in ["stop", "стоп"]:
			break

		try:
			user_request = Request(request=user_input, storages=storages)
			courier = Courier(request=user_request, storages=storages)
			courier.delivery_action()
		except BaseError as error:
			print(error.message)


if __name__ == '__main__':
	main()