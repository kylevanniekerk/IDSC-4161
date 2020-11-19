# -*- coding: utf-8 -*-
year = int(input('Enter year: '))
leap = int(year % 4)
cent = int(year % 100)
leapcent = int(year % 400)

if cent == 0:
    if leapcent == 0:
        print('{0} is a leap year ' .format(year))
    else:
        print('{0} is a common year ' .format(year))
elif leap == 0:
    print('{0} is a leap year ' .format(year))
else:
    print('{0} is a common year ' .format(year))
