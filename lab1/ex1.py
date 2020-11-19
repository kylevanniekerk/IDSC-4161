# -*- coding: utf-8 -*-

name = input('Please enter customer name: ')
labor_hours = float(input('Please enter labor hours: '))
cost = float(input('Please enter cost of parts and supplies: '))



labor_cost = float(labor_hours * 35)
parts_cost = float(cost * 0.07 + cost)
total_cost = float(labor_cost + parts_cost)

print(' Customer:{0} ,  Labor cost:{1:.2f} ,  Parts cost:{2:.2f} ,  Total cost:{3:.2f} '.format(name, labor_cost, parts_cost, total_cost))

