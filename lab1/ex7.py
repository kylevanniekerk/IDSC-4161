# -*- coding: utf-8 -*-
velo = int(input('Enter initial velocity(fps): '))
h = int(input('Enter initial height(feet): '))

fheight = float(-144 + velo*3 + h)

print('The height after 3 seconds is: {0:.1f} ft '.format(fheight))

