# -*- coding: utf-8 -*-

miles = float(input('Enter miles: '))
yards = float(input('Enter yards: '))
feet = float(input('Enter feet: '))
inches = float(input('Enter inches: '))

totinches = float((miles*63360) + (yards*36) + (feet*12) + inches)
centimeters = float(totinches/ 0.3937)

km = float(centimeters//100000)
centimeters = centimeters % 10000
meters = float(centimeters// 100)
centimeters = centimeters % 100

print('The metric length is: , {0:.2f} kilometers, {1:.2f} meters, {2:.2f} centimeters '.format(km, meters, centimeters))

