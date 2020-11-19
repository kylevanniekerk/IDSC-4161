work = float(input('Please enter the number of hours worked: '))
hwage = float(input('Please enter the hourly wage: '))

if work <= 40 :
    gross = float(work * hwage)
    print('Gross pay is ${0:.2f} ' .format(gross))
else:
    grossplus = float((work-40)*(hwage*1.5) + (40 * hwage))
    print('Gross pay is ${0:.2f} ' .format(grossplus))

