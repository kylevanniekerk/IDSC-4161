def average_steps(filename, month):
    avesteps = int(0)
    with open(filename, 'r') as f:
        lines = f.read().split('\n')
        jan = lines[0:31]
        feb = lines[31:59]
        mar = lines[59:90]
        apr = lines[90:120]
        may = lines[120:151]
        jun = lines[151:181]
        jul = lines[181:212]
        aug = lines[212:243]
        sep = lines[243:273]
        octo = lines[273:304]
        nov = lines[304:334]
        dec = lines[334:365]
        if month == 1:
            for steps in jan:
                avesteps += int(steps)/31
        elif month == 2:   
            for steps in feb:
                avesteps += int(steps)/28
        elif month == 3:   
            for steps in mar:
                avesteps += int(steps)/31
        elif month == 4:   
            for steps in apr:
                avesteps += int(steps)/30
        elif month == 5:   
            for steps in may:
                avesteps += int(steps)/31
        elif month == 6:   
            for steps in jun:
                avesteps += int(steps)/30
        elif month == 7:   
            for steps in jul:
                avesteps += int(steps)/31
        elif month == 8:   
            for steps in aug:
                avesteps += int(steps)/31
        elif month == 9:   
            for steps in sep:
                avesteps += int(steps)/30
        elif month == 10:   
            for steps in octo:
                avesteps += int(steps)/31
        elif month == 11:   
            for steps in nov:
                avesteps += int(steps)/30
        elif month == 12:   
            for steps in dec:
                avesteps += int(steps)/31
            
    return round(avesteps, 1)
            
                
            
                
                

