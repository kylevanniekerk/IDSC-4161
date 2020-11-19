cover = float(input('Enter percentage cloud cover: '))

if cover >= 0  and cover <= 30:
    print('clear ')
elif cover > 30 and cover <= 70:
    print('partly cloudy ')
elif cover > 70 and cover <= 99:
    print('mostly cloudy ')
else:
    print('overcast ')

