num = int(input('Whole dollar amount(ex. $500): '))

def double_or_1(num):
    count = 0
    while num != 1:
        count += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num -= 1                  
    return count

print('{0}'.format(double_or_1(num)))
        
    

