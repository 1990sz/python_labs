#!/usr/bin/env python3
# -*- coding: utf-8 -*-

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

zoo.insert(2,'bear')
print(zoo)

birds = ['rooster', 'ostrich', 'lark', ]

zoo.extend(birds)
print(zoo)

zoo.remove('elephant')
print(zoo)

print(zoo.index('lion')+1)
print(zoo.index('lark')+1)
