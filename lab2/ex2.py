package = input('Enter package (A, B or C): ')
nonp = input('NonProfit? (y or n): ')
hours = int(input('Hours used: '))
total = float(0)
saveb = float(0)
savec = float(0)

if package == 'A':
    if hours <= 10:
        total += 9.95
        saveb += 14.95
        savec += 19.95
        if nonp == 'y':
            total = total - (total*0.2)
            saveb = saveb - (saveb*0.2)
            savec = savec - (savec*0.2)
    elif hours > 10 and hours <= 20:
        total += 9.95 + ((hours - 10)*2)
        saveb += 14.95 
        savec += 19.95
        if nonp == 'y':
            total = total - (total*0.2)
            saveb = saveb - (saveb*0.2)
            savec = savec - (savec*0.2)
    elif hours > 20 :
        total += 9.95 + ((hours - 10)*2)
        saveb += 14.95 + ((hours - 20)*1)
        savec += 19.95
        if nonp == 'y':
            total = total - (total*0.2)
            saveb = saveb - (saveb*0.2)
            savec = savec - (savec*0.2)
            
    print('Your total is ${0:.2f}'.format(total))
    if saveb < total:
        newsaveb = float(total - saveb)
        print('You would have saved ${0:.2f} with package B'.format(newsaveb))
    if saveb > total:
        print('No savings with package B.')
    if savec < total:
        newsavec = float(total - savec)
        print('you would have saved ${0:.2f} with package C'.format(newsavec))
    if savec > total:
        print('No savings with package C.')
elif package == 'B':
    if hours <= 20:
        total += 14.95
        savec += 19.95
        if nonp == 'y':
            total = total - (total*0.2)
            savec = savec - (savec*0.2)
    elif hours > 20:
        total += 14.95 + ((hours - 20)*1)
        savec += 19.95
        if nonp == 'y':
            total = total - (total*0.2)
            savec = savec - (savec*0.2)
            
    print('Your total is ${0:.2f}'.format(total))
    if savec < total:
        newsavec = float(total - savec)
        print('you would have saved ${0:.2f} with package C'.format(newsavec))
    elif savec > total:
        print('No savings with package C.')
elif package == 'C':
    total += 19.95
    if nonp == 'y':
        total = total - (total*0.2)
        
    print('Your total is ${0:.2f}'.format(total))
    
    

