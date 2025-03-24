import tkinter as tk
from tkinter import ttk
from CarPaint import CarPaint


class PaintCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор покраски автомобиля")
        self.root.geometry("400x400")

        # Создаем основной контейнер
        self.mainframe = ttk.Frame(root, padding="10")
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Переменные для хранения выбора
        self.color_var = tk.StringVar()
        self.details_vars = []

        # Создаем элементы интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Выбор цвета
        ttk.Label(self.mainframe, text="Выберите цвет:").grid(column=0, row=0, sticky=tk.W, pady=5)

        colors = [color[0] for color in CarPaint.colorsMultipliers]
        self.color_combobox = ttk.Combobox(
            self.mainframe,
            textvariable=self.color_var,
            values=colors,
            state="readonly"
        )
        self.color_combobox.grid(column=0, row=1, sticky=(tk.W, tk.E), pady=5)
        self.color_combobox.current(0)

        # Выбор деталей
        ttk.Label(self.mainframe, text="Выберите детали для покраски:").grid(column=0, row=2, sticky=tk.W, pady=5)

        details_frame = ttk.Frame(self.mainframe)
        details_frame.grid(column=0, row=3, sticky=(tk.W, tk.E))

        for i, (detail, _) in enumerate(CarPaint.detailsMultipliers):
            var = tk.BooleanVar()
            cb = ttk.Checkbutton(details_frame, text=detail, variable=var)
            cb.grid(column=0, row=i, sticky=tk.W, pady=2)
            self.details_vars.append((detail, var))

        # Кнопка расчета
        ttk.Button(
            self.mainframe,
            text="Рассчитать стоимость",
            command=self.calculate_price
        ).grid(column=0, row=4, pady=10)

        # Результат
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

        car_paint = CarPaint(color, selected_details)
        price = car_paint.get_price()

        self.result_var.set(f"Итоговая стоимость: {price:.2f} руб.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintCalculatorApp(root)
    root.mainloop()