desc = input('Description of the item: ')
cost = float(input('Cost of the item: '))
life = int(input('Estimated life of the item in whole years: '))
meth = int(input('Depreciation method (1 = straight line, 2 = double declining balance): '))
begin = float(cost)
dep = float(0)
end = float(cost)
eyear = int(0)

year = 'Year'
b = 'Begin'
d = 'Dep'
e = 'end'

print('Depreciation schedule for: {0}'.format(desc))
print('')
print('{0:7} {1:10} {2:10} {3}'.format(year, b, d, e))

for eyear in range(life + 1):
    print('{0:2d} {1:10.2f} {2:10.2f} {3:10.2f}'.format(eyear, begin, dep, end))
    if meth == 2:
        begin -= dep
        dep = begin * 2/life
        end = begin - dep
        if eyear == (life - 1):
            dep = begin
            end = begin - dep
    else:
        begin -= dep
        dep = cost * 1/life
        end = begin - dep
         
