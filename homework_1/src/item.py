class Item:
    pay_rate = 0.85  # Установленая скидка на товар 15%
    all = []  # Cписок для хранения экземпляров класса

    def __init__(self, name: str, price: float, amount: int) -> None:
        self.name = name
        self.price = price
        self.amount = amount
        self.all.append(self)

    def calculate_total_price(self):
        """"Подсчет общей стоимость товара"""
        return f"{self.price * self.amount}"

    def apply_discount(self):
        """"Приминение скидки на товар"""
        self.price *= self.pay_rate
