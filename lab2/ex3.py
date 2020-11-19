denom = int(input('Please enter the maximum denominator: '))
total = float(0)
loop = int(0)

for loop in range (1, denom + 1):
    total += 1/loop

print('the sum is {0:.11f}.'.format(total))

