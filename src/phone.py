from src.item import Item

class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param sim_quantity: Количество слотов сим-карт.
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
