#!/usr/bin/env python3
# -*- coding: utf-8 -*-

my_family = ['мама', 'папа',  'я', 'брат']


my_family_height = [
    ['Алёна',165],
    ['Андрей',193],
    ['Федя',180],
    ['Тимофей',155]
]

print('Рост: '+my_family[1]+' -', my_family_height[1][1],'см.')

sum_height = 0
sum_height += my_family_height[0][1]
sum_height += my_family_height[1][1]
sum_height += my_family_height[2][1]
sum_height += my_family_height[3][1]

print('Общий рост моей семьи -', sum_height, 'см.')
