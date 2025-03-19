class CarPaint:
    base_price = 12000  # используем base_price, чтобы не менять исходную цену

    def __init__(self, color, details):
        self.color = color
        self.details = details

    colorsMultipliers = {
        'Белый': 1,
        'Синий': 1,
        'Желтый': 1.1,
        'Красный': 1,
        'Перламутровый': 1.2,
        'Серый металлик': 1.3
    }

    detailsMultipliers = {
        'Капот': 1,
        'Передняя дверь': 1.2,
        'Задняя дверь': 1.1,
        'Передний бампер': 1,
        'Задний бампер': 1,
        'Крыша': 1.1
    }

    def get_price(self):
        total_price = self.base_price
        details_description = []

        for detail in self.details:
            multiplier = self.detailsMultipliers.get(detail, 1)
            total_price *= multiplier
            details_description.append(f"{detail} (x{multiplier})")

        color_multiplier = self.colorsMultipliers.get(self.color, 1)
        total_price *= color_multiplier

        print(f"Базовая цена: {self.base_price}")
        print(f"Детали: {', '.join(details_description)}")
        print(f"Цвет: {self.color} (x{color_multiplier})")
        print(f"Итого: {round(total_price, 2)}")

        return round(total_price, 2)