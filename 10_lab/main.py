import tkinter as tk
from tkinter import Tk
from tkinter import messagebox
from tkinter import filedialog
import datetime
from openpyxl import Workbook
from docx import Document

class FuelCalculationApp:
    def __init__(self, master):
        self.master = master
        master.title("Расчет расхода топлива")

        # Переменные для ввода данных пользователем
        self.car_type = tk.StringVar()
        self.fuel_consumption = tk.StringVar()
        self.distance = tk.StringVar()
        self.weight = tk.StringVar()
        self.passengers = tk.StringVar()
        self.price = tk.StringVar()


        # Создание виджетов для ввода данных
        tk.Label(master, text="Выберите тип автомобиля:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.car_type.set("Легковой")
        tk.OptionMenu(master, self.car_type, "Легковой", "Грузовой", "Пассажирский").grid(row=0, column=1, padx=5, pady=5)

        tk.Label(master, text="Расход топлива на 100 км:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(master, textvariable=self.fuel_consumption).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(master, text="Расстояние (км):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(master, textvariable=self.distance).grid(row=2, column=1, padx=5, pady=5)

        tk.Label(master, text="Груз (кг):").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(master, textvariable=self.weight).grid(row=3, column=1, padx=5, pady=5)

        tk.Label(master, text="Количество пассажиров:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(master, textvariable=self.passengers).grid(row=4, column=1, padx=5, pady=5)

        tk.Label(master, text="Цена топлива за литр:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(master, textvariable=self.price).grid(row=5, column=1, padx=5, pady=5)

        # Создание кнопки для расчета и отображения результатов
        tk.Button(master, text="Рассчитать", command=self.calculate).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(master, text="Сохранить", command=self.save).grid(row=6, column=1, padx=5, pady=5)


    def calculate(self):
        try:
            # Получение данных из полей ввода
            car_type = self.car_type.get()
            fuel_consumption = float(self.fuel_consumption.get())
            distance = float(self.distance.get())
            weight = float(self.weight.get())
            passengers = int(self.passengers.get())
            price = float(self.price.get())

            coef = 1
            speed = 60

            if car_type == "Легковой":
                coef = 1

            elif car_type == "Пассажирский":
                coef = 1.2
            elif car_type == "Грузовой":
                coef = 1.5


            self.fuel_cost = (fuel_consumption * distance / 100 + weight * coef) * price + passengers * coef
            self.travel_time = distance / speed

            messagebox.showinfo("Результат расчета", f"Стоимость топлива: {self.fuel_cost:.2f} руб.\n"
                                                     f"Время поездки: {self.travel_time:.2f} ч.")



        except ValueError:
            messagebox.showerror("Ошибка", "Неверные значения")




    def save(self):
        try:
            filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Exel files", ".xlsx")])
            if filename:
                wb = Workbook()
                ws = wb.active

                data = [
                    ["Тип автомобиля", self.car_type.get()],
                    ["Расход топлива(на 100 км)", float(self.fuel_consumption.get())],
                    ["Расстояние(в км)", float(self.distance.get())],
                    ["Груз (кг)", float(self.weight.get())],
                    ["Кол-во пассажиров", int(self.passengers.get())],
                    ["Цена за литр топлива", float(self.price.get())],
                    ["Стоимость поездки", self.fuel_cost],
                    ["Время поездки", self.travel_time]
                ]

                for row in data:
                    ws.append(row)

                wb.save(filename)
        except Exception as _:
            print(_)



root = Tk()
mugui = FuelCalculationApp(root)

root.mainloop()