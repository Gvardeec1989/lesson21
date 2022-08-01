from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, name, count):  # увеличивает запас items
        pass

    @abstractmethod
    def remove(self, name, count):  # уменьшает запас items
        pass

    @abstractmethod
    def get_free_space(self):  # вернуть количество свободных мест
        pass

    @abstractmethod
    def get_items(self):  # возвращает сожержание склада в словаре {товар: количество}
        pass

    @abstractmethod
    def get_unique_items_count(self):  # возвращает количество уникальных товаров.
        pass


class Store(Storage):

    def __init__(self, items: dict, capacity=100):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, count):            # добавление
        if name in self.__items.keys():
            if self.get_free_space() >= count:
                print("товар добавлен")
                self.__items[name] += count
                return True
            else:
                print("недостаточно товара на складе")
                return False
        else:
            if self.get_free_space() >= count:
                print("товар добавлен")
                self.__items[name] = count
                return True
            else:
                print("недостаточно товара на складе")
                return False

    def remove(self, name, count):         # убавление
        if self.__items[name] > count:
            self.__items[name] -= count
        else:
            return "Недостаточно товара на складе"

    def get_free_space(self):               # вернуть количество свободных мест
        free_place = 0
        for value in self.__items.values():
            free_place += value
        return self.__capacity - free_place

    def get_items(self):                    # возвращает содержание склада в словаре {товар: количество}
        return self.__items

    def get_unique_items_count(self):       # возвращает количество уникальных товаров.
        return len(self.__items.keys())

    def __str__(self):
        st = "\n"
        for key, value in self.__items.items():
            st += f"{key}: {value}\n"
        return st


class Shop(Store):
    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, count):                     # увеличивает запас items с учетом лимита capacity
        if self.get_unique_items_count() >= 5:
            print("Добавление невозможно")
            return "Добавление невозможно"
        else:
            super().add(name, count)

# методы remove\get_free_space()\get_items()\get_unique_items_count() - исполняются из Store


class Request:
    def __init__(self, request_str):
        req_list = request_str.split()
        action = req_list[0]
        self.__count = int(req_list[1])
        self.__item = req_list[2]
        if action == "Доставить":
            self.__from = req_list[4]
            self.__to = req_list[6]
        elif action == "Забрать":
            self.__from = req_list[4]
            self.__to = None
        elif action == "Привезти":
            self.__to = req_list[4]
            self.__from = None

    def move(self):
        if self.__to and self.__from:
            if eval(self.__to).add(self.__item, self.__count):
                eval(self.__from).remove(self.__item, self.__count)
        if self.__to:
            eval(self.__to).add(self.__item, self.__count)
        if self.__from:
            eval(self.__from).remove(self.__item, self.__count)

storage_1 = Store(items={"телефон": 10, "компьютер": 10, "приставка": 10})
storage_2 = Store(items={"телефон": 10, "компьютер": 10, "холодильник": 10})
shop_1 = Shop(items={"телефон": 3, "компьютер": 3, "холодильник": 3})

while True:
    print("в наличие:")
    print(f"storage_1: {storage_1}")
    print(f"storage_2: {storage_2}")
    print(f"shop_1: {shop_1}")
    user_text = input("введите команду:\n")       # Забрать 4 телефон из storage_2
    if user_text == "стоп":
        break
    else:
        try:
            req = Request(user_text)
            req.move()
        except Exception as e:
            print("произошла ошибка")