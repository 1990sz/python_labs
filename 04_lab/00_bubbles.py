#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd
import random, time
sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
sd.circle(center_position=sd.get_point(600, 300), radius=100, width=5)
sd.circle(center_position=sd.get_point(600, 300), radius=95, width=5)
sd.circle(center_position=sd.get_point(600, 300), radius=90, width=5)


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def draw_bubble(center, step, color):
    radius = 100
    width = 5
    for i in range(3):
        sd.circle(center_position=center, radius=radius, width=width, color=color)
        radius -= step
        width += 2


# Нарисовать 10 пузырьков в ряд
start_x = 1200 // 2 - 5 * 100

for i in range(10):
    center = sd.get_point(start_x + i * 100, 600 // 2)
    draw_bubble(center, 5, sd.COLOR_ORANGE)

# Нарисовать три ряда по 10 пузырьков
for i in range(3):
    y = 600 - (i + 1) * (20 * 2 + 60) - 20
    for j in range(10):
        x = (j + 1) * (20 * 2 + 60) - 20
        center_position = sd.get_point(x, y)
        sd.circle(center_position, 20, sd.COLOR_ORANGE)
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    # генерируем случайную точку на экране
    x = random.randint(0, sd.resolution[0])
    y = random.randint(0, sd.resolution[1])
    center = sd.get_point(x, y)

    # генерируем случайный радиус и цвет
    radius = random.randint(10, 50)
    color = sd.random_color()

    # рисуем пузырек
    sd.circle(center_position=center, radius=radius, color=color, width=2)

    # задержка на 0.1 секунду
    time.sleep(0.1)

sd.pause()
