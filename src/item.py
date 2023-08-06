import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = float(price)
        self.quantity = int(quantity)
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {int(self.price)}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @property
    def name(self) -> str:
        """
        Getter для получения имени товара.
        """
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """
        Setter для имени товара.
        """
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        with open('../src/items.csv', 'r', encoding='utf8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                Item(row['name'], cls.string_to_number(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(string: str) -> float:
        return int(float(string))
