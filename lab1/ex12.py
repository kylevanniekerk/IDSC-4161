a = float(input('Enter value for a: '))
b = float(input('Enter value for b: '))
c = float(input('Enter value for c: '))

equation = float(b**2 -4 * a * c)

if equation > 0:
    big1 = float((-b + (b**2 -4 * a * c)**(0.5)) / (2*a))
    big2 = float((-b - (b**2 -4 * a * c)**(0.5)) / (2*a))
    print('Solution: {0:.2f}, {1:.2f}' .format(big1, big2))
elif equation == 0:
    zero = float(-b / (2*a))
    print('Solution: {0:.2f} ' .format(zero))
else:
    print('No solutions. ')
    

