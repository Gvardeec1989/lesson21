from abc import ABC, abstractmethod


class Storage(ABC):

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

    def __int__(self, items: dict, capacity=100):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, count):            # добавление
        if name in self.__items.keys():
            if self.get_free_space() >= count:
                print("Товар добален")
                self.__items[name] += count
            else:
                return "На складе недостаточно места"
        else:
            if self.get_free_space() >= count:
                print("Товар добален")
                self.__items[name] = count
            else:
                return "На складе недостаточно места"

    def remove(self, name, count):         # убавление
        if self.__items[name] <= count:
            print("Нужное колличество есть на складе")
            self.__items[name] -= count
        else:
            return "Недостаточно товара"

    def _get_free_space(self):               # вернуть количество свободных мест
        free_place = 0
        for value in self.__items.values():
            free_place += value
        return self.__capacity - free_place

    def get_items(self):                    # возвращает содержание склада в словаре {товар: количество}
        return self.__items

    def _get_unique_items_count(self):       # возвращает количество уникальных товаров.
        return len(self.__items.keys())

    def __str__(self):
        st = "\n"
        for key, value in self.__items.items():
            st += f"{key}: {value}\n"
        return st


class Shop(Store):
    def __int__(self, items: dict, capacity=20):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, count):                     # увеличивает запас items с учетом лимита capacity
        if self.get_unique_items_count() >= 5:
            return "Добавление невозможно"
        else:
            super().add(name, count)


class Request:
    def __int__(self, request_str):
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
        if self.__to:
            eval(self.__to).add(self.__item, self.__count)
        if self.__from:
            eval(self.__from).remove(self.__item, self.__count)


storage_1 = Store(items={"Яблоки": 10, "Печенье": 10, "Крупа": 10})
storage_2 = Store(Items={"Компьютер": 10, "Наушники": 10, "Лодка": 10})
shop_1 = Shop(items={"Яблоки": 3, "Печенье": 3, "Крупа": 3})

print(storage_2)
