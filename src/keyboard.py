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


class Keyboard(MixinLang):

    def __init__(self, name: str, price: float, amount: int) -> None:
        super().__init__()
        self.name = name
        self.price = price
        self.amount = amount
