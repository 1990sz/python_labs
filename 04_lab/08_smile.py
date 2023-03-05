#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
def draw_smiley(x, y, color):
    # рисуем голову
    sd.circle(sd.get_point(x, y), 50, color, 0)
    # рисуем глаза
    left_eye_center = sd.get_point(x - 20, y + 10)
    right_eye_center = sd.get_point(x + 20, y + 10)
    sd.circle(left_eye_center, 10, color, 0)
    sd.circle(right_eye_center, 10, color, 0)
    # рисуем зрачки
    left_pupil_center = sd.get_point(x - 20, y + 12)
    right_pupil_center = sd.get_point(x + 20, y + 12)
    sd.circle(left_pupil_center, 5, sd.COLOR_BLACK, 0)
    sd.circle(right_pupil_center, 5, sd.COLOR_BLACK, 0)
    # рисуем рот
    mouth_left = sd.get_point(x - 20, y - 25)
    mouth_right = sd.get_point(x + 20, y - 25)
    sd.line(mouth_left, mouth_right, sd.COLOR_BLACK, 4)


for i in range(10):
    x = random.randint(100, 500)
    y = random.randint(100, 500)
    color = random.choice([sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_BLUE])
    draw_smiley(x, y, color)


sd.pause()
