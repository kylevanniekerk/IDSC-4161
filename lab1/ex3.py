# -*- coding: utf-8 -*-

depo = float(input('Enter annual deposit: '))
r = float(input('Enter rate: '))

bal1 = float(depo*((1 + r/100)))
bal2 = float(bal1*((1 + r/100)))
bal3 = float(bal2*((1 + r/100)))
bal = float(bal1 + bal2 + bal3)

print('After 3 years, balance is: ${0:.2f}'.format(bal))

