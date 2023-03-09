#!/usr/bin/env python3
# -*- coding: utf-8 -*-


radius = 42


pi = 3.1415926
print(round(pi*radius**2,4))


point = (23, 34)



distance = round(((0-point[0])**2+(0-point[1])**2)**0.5, 2)
print(distance <= radius)



point_2 = (30, 30)


distance = round(((0-point_2[0])**2+(0-point_2[1])**2)**0.5, 2)
print(distance <= radius)




