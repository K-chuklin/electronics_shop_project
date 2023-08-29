import csv


class InstantiateCSVError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Файл item.csv поврежден'


class Item:
    pay_rate = 0.85  # Установленая скидка на товар 15%
    all = []  # Cписок для хранения экземпляров класса

    def __init__(self, name: str, price: float, amount: int) -> None:
        self.__name = name
        self.price = price
        self.amount = amount
        self.all.append(self)

    def __str__(self):
        return f'{self.__name}'

    def __repr__(self):
        return f"{__class__.__name__}('{self.__name}', {self.price}, {self.amount})"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно '
                             f'только объекты {self.__class__.__name__} '
                             'и дочерние от них.')
        return self.amount + other.amount

    @classmethod
    def instantiate_from_csv(cls):
        try:
            cls.all = []
            with open('../src/items.csv', newline='', encoding='Windows-1251') as f:
                data = csv.DictReader(f)
                try:
                    for item in data:
                        cls(item['name'], float(item['price']), int(item['quantity']))
                except KeyError:
                    raise InstantiateCSVError("Файл item.csv поврежден")
        except FileNotFoundError:
            print("Отсутствует файл item.csv")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 30:
            self.__name = name[:30]
        else:
            self.__name = name

    def calculate_total_price(self):
        """"Подсчет общей стоимость товара"""
        return f"{self.price * self.amount}"

    def apply_discount(self):
        """"Приминение скидки на товар"""
        self.price *= self.pay_rate
