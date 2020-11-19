# -*- coding: utf-8 -*-
h1 = int(input('Enter time 1 hours: '))
m1 = int(input('Enter time 1 minutes: '))
h2 = int(input('Enter time 2 hours: '))
m2 = int(input('Enter time 2 minutes: '))
tothours = h1 + h2
totmin = m1 + m2

tot = int(tothours*60 + totmin)
fh = int(tot / 60)
fm = int(tot % 60)

print('Total time is: {0}:{1}' .format(fh, fm)) 


