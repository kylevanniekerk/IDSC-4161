# -*- coding: utf-8 -*-
begodo = int(input('Enter beginning odometer: '))
endodo = int(input('Enter beginning odometer: '))
gallon = int(input('Enter gallons: '))

reading = float((endodo - begodo) / gallon)

print('Fuel efficiency: {0:.1f} miles per gallon ' .format(reading))

