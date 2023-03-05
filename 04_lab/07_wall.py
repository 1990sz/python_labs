#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

# Размер кирпича
BRICK_WIDTH = 100
BRICK_HEIGHT = 50

# Размер стены
WALL_WIDTH = 800
WALL_HEIGHT = 600

# Цвета кирпичей
BRICK_COLORS = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN]

# Рисуем стену
for row in range(0, WALL_HEIGHT, BRICK_HEIGHT):
    # Смещение строки кирпичей на половину размера кирпича вправо на четных рядах и на половину размера кирпича влево на нечетных рядах
    offset = int(BRICK_WIDTH / 2 if row // BRICK_HEIGHT % 2 == 0 else -BRICK_WIDTH / 2)
    for row in range(offset, WALL_HEIGHT, BRICK_HEIGHT):
        if row // BRICK_HEIGHT % 2 == 0:  # каждый четный ряд
            for col in range(offset, WALL_WIDTH, BRICK_WIDTH):
                sd.rectangle(sd.get_point(col, row), sd.get_point(col + BRICK_WIDTH, row + BRICK_HEIGHT),
                             color=sd.COLOR_ORANGE, width=1)
        else:  # каждый нечетный ряд
            for col in range(offset + BRICK_WIDTH // 2, WALL_WIDTH, BRICK_WIDTH):
                sd.rectangle(sd.get_point(col, row), sd.get_point(col + BRICK_WIDTH, row + BRICK_HEIGHT),
                             color=sd.COLOR_ORANGE, width=1)

sd.pause()
