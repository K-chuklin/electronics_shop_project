import csv


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
        if __class__.__name__ == 'Item' or __class__.__name__ == 'Phone':
            return self.amount + other.amount

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open('../homework_2/src/items.csv', newline='', encoding='Windows-1251') as csvfile:
            data = csv.DictReader(csvfile)
            for item in data:
                cls(item['name'], float(item['price']), int(item['quantity']))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    def calculate_total_price(self):
        """"Подсчет общей стоимость товара"""
        return f"{self.price * self.amount}"

    def apply_discount(self):
        """"Приминение скидки на товар"""
        self.price *= self.pay_rate
