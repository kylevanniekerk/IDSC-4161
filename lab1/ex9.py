
miliTime = int(input("Enter a time in hh:mm (military) format: "))
    
    if len(miliTime) == 3:
        hours = miliTime[0]
        minutes = miliTime[2]
        
    elif len(miliTime) == 4:
        if miliTime[0:2] >= 10:
            hours = militime[0:2]
            minutes = militime[3]
            
            if minutes < 10:
                minutes = 0 + minutes
        else:
            hours = miliTime[0]
            minutes = militime[2:]
           
    else:
        hours = miliTime[0:2]
        minutes = miliTime[3:]
    setting = AM
    if hours > 12:
        setting = PM
        hours -= 12
    print(hours + ":" + minutes + setting)