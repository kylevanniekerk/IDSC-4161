invest = float(input('Please enter your initial investment: '))
rate = float(input('Please enter annual interest rate (ex. 2.5): '))
payout = float(input('Please enter the monthly annuity payout: '))
months = int(0)
interest = float((rate/12)/100 + 1)
bal = float(invest)

while bal > payout:
     bal = bal * interest - payout
     months += 1

print('After {0} months your balance is ${1:.2f}.'.format(months, bal))
