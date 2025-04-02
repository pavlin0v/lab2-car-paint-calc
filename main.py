# РЕЛИЗ 0.3
import tkinter as tk
from tkinter import ttk
from CarPaint import CarPaint


class PaintCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор покраски автомобиля")
        self.root.geometry("400x400")

        self.mainframe = ttk.Frame(root, padding="10")
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        self.color_var = tk.StringVar()
        self.details_vars = []

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.mainframe, text="Выберите цвет:").grid(column=0, row=0, sticky=tk.W, pady=5)

        # Безопасное получение списка цветов
        colors = []
        if hasattr(CarPaint, 'colorsMultipliers'):
            try:
                colors = [color[0] for color in CarPaint.colorsMultipliers]
            except (IndexError, TypeError):
                colors = ["Стандартный"]  # значение по умолчанию

        self.color_combobox = ttk.Combobox(
            self.mainframe,
            textvariable=self.color_var,
            values=colors,
            state="readonly"
        )
        self.color_combobox.grid(column=0, row=1, sticky=(tk.W, tk.E), pady=5)
        self.color_combobox.current(0)

        ttk.Label(self.mainframe, text="Выберите детали для покраски:").grid(column=0, row=2, sticky=tk.W, pady=5)

        details_frame = ttk.Frame(self.mainframe)
        details_frame.grid(column=0, row=3, sticky=(tk.W, tk.E))

        # Безопасная обработка detailsMultipliers
        if hasattr(CarPaint, 'detailsMultipliers'):
            for i, item in enumerate(CarPaint.detailsMultipliers):
                try:
                    # Пытаемся получить название детали (первый элемент)
                    detail = item[0] if isinstance(item, (tuple, list)) else str(item)
                    var = tk.BooleanVar()
                    cb = ttk.Checkbutton(details_frame, text=detail, variable=var)
                    cb.grid(column=0, row=i, sticky=tk.W, pady=2)
                    self.details_vars.append((detail, var))
                except Exception as e:
                    print(f"Ошибка при создании чекбокса для элемента {item}: {e}")
        else:
            ttk.Label(details_frame, text="Нет данных о деталях").grid(column=0, row=0)

        ttk.Button(
            self.mainframe,
            text="Рассчитать стоимость",
            command=self.calculate_price
        ).grid(column=0, row=4, pady=10)

        self.result_var = tk.StringVar()
        ttk.Label(
            self.mainframe,
            textvariable=self.result_var,
            font=('Arial', 12, 'bold'),
            foreground='blue'
        ).grid(column=0, row=5, pady=10)

    def calculate_price(self):
        color = self.color_var.get()
        selected_details = [detail for detail, var in self.details_vars if var.get()]

        if not selected_details:
            self.result_var.set("Ошибка: выберите хотя бы одну деталь!")
            return

        try:
            car_paint = CarPaint(color, selected_details)
            price = car_paint.get_price()
            self.result_var.set(f"Итоговая стоимость: {price:.2f} руб.")
        except Exception as e:
            self.result_var.set(f"Ошибка расчета: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintCalculatorApp(root)
    root.mainloop()