class CarPaintingCalculator:
    BASE_PRICE = 12000  # Базовая стоимость окраски одной детали

    COLOR_COEFFICIENTS = {
        "Белый": 1.0,
        "Синий": 1.0,
        "Желтый": 1.1,
        "Красный": 1.0,
        "Перламутровый": 1.2,
        "Серый металлик": 1.3
    }

    PART_COEFFICIENTS = {
        "Капот": 1.0,
        "Передняя дверь": 1.2,
        "Задняя дверь": 1.1,
        "Передний бампер": 1.0,
        "Задний бампер": 1.0,
        "Крыша": 1.1
    }

    @staticmethod
    def calculate_price(part_name, color):
        """ Рассчитывает стоимость покраски детали """
        part_coef = CarPaintingCalculator.PART_COEFFICIENTS.get(part_name, 1.0)
        color_coef = CarPaintingCalculator.COLOR_COEFFICIENTS.get(color, 1.0)
        return CarPaintingCalculator.BASE_PRICE * part_coef * color_coef


def main():
    print("Калькулятор стоимости окраски автомобиля")
    
    part = input("Введите название детали (например, Капот, Передняя дверь, Крыша): ").strip()
    color = input("Введите цвет (например, Белый, Красный, Перламутровый): ").strip()

    price = CarPaintingCalculator.calculate_price(part, color)

    print(f"Стоимость покраски детали '{part}' в цвет '{color}' составит: {price} руб.")


if __name__ == "__main__":
    main()
