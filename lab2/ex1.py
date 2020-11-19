
people = abs(int(input('Enter # of people: ')))
hot = abs(int(input('Enter # of hot dogs per person: ')))

hotdogs = people * hot

if hotdogs <= 10:
    hreq = 1
elif hotdogs <= 20:
    hreq = 2
elif hotdogs <= 30:
    hreq = 3
elif hotdogs <= 40:
    hreq = 4
elif hotdogs <= 50:
    hreq = 5
else:
    print('Too many hotdogs needed')

if hotdogs <= 10:
    hleft = 10 - hotdogs
elif hotdogs <= 20:
    hleft = 20 - hotdogs
elif hotdogs <= 30:
    hleft = 30 - hotdogs
elif hotdogs <= 40:
    hleft = 40 - hotdogs
elif hotdogs <= 50:
    hleft = 50 - hotdogs

if hotdogs <= 8:
    brequ = 1
elif hotdogs <= 16:
    brequ = 2
elif hotdogs <= 24:
    brequ = 3
elif hotdogs <= 32:
    brequ = 4
elif hotdogs <= 40:
    brequ = 5
else:
    print('Too many hotdogs needed')

if hotdogs <= 8:
    bleft = 8 - hotdogs
elif hotdogs <= 16:
    bleft = 16 - hotdogs
elif hotdogs <= 24:
    bleft = 24 - hotdogs
elif hotdogs <= 32:
    bleft = 32 - hotdogs
elif hotdogs <= 40:
    bleft = 40 - hotdogs
    
print('{0} hot dog package(s) required; {1} hot dogs left over!'.format(hreq,hleft))
print('{0} bun package(s) required; {1} bun left over!'.format(brequ,bleft))


