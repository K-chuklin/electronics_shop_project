from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, amount: int, number_of_sim: int) -> None:
        super().__init__(name, price, amount)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim >= 1:
            return self.__number_of_sim == number_of_sim
        raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.amount}, {self.number_of_sim})"

    def __add__(self, other):
        if __class__.__name__ == 'Item' or __class__.__name__ == 'Phone':
            return self.amount + other.amount

