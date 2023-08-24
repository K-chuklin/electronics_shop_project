from src.item import Item


class MixinLang:

    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        if language == "RU" or language == "EN":
            self.__language = language
        else:
            raise AttributeError

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
            return self.__language
        self.__language = "EN"
        return self


class Keyboard(Item, MixinLang):

    def __init__(self, name: str, price: float, amount: int, language="EN") -> None:
        super().__init__(name, price, amount)
        self.name = name
        self.price = price
        self.amount = amount
        self.__language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        if language == "RU" or language == "EN":
            self.__language = language
        raise AttributeError("property 'language' of 'Keyboard' object has no setter")

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
            return self.__language
        self.__language = "EN"
        return self

    def __str__(self):
        return f'{self.name}'
