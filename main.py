class CarPaint:
    price = 12000

    def __init__(self, color, details):
        self.color = color
        self.details = details

    colorsMultipliers = (
        ('Белый', '1'),
        ('Синий', '1'),
        ('Желтый', '1.1'),
        ('Красный', '1'),
        ('Перламутровый', '1.2'),
        ('Серый металлик', '1.3')
    )

    detailsMultipliers = (
        ('Капот', '1'),
        ('Передняя дверь', '1.2'),
        ('Задняя дверь', '1.1'),
        ('Передний бампер', '1'),
        ('Задний бампер', '1'),
        ('Крыша', '1.1')
    )

    def get_price(self):
        for detail in self.details:
            for detailMultiplier in self.detailsMultipliers:
                if detail == detailMultiplier[0]:
                    self.price *= float(detailMultiplier[1])
        for colorMultiplier in self.colorsMultipliers:
            if self.color == colorMultiplier[0]:
                self.price *= float(colorMultiplier[1])
        return self.price

carPrint = CarPaint('Белый', ['Капот', 'Передняя дверь'])
print(carPrint.get_price())
