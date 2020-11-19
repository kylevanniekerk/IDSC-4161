# -*- coding: utf-8 -*-
cycling = int(input('Enter hours cycling: '))
running = int(input('Enter hours running: '))
swim = int(input('Enter hours swimming: '))

calcyc = cycling * 200
calrun = running * 475
calswim = swim * 275
totcal = calcyc + calrun + calswim 

lost = totcal / 3500

print('Total pounds lost: {0:.1f}'.format(lost))
