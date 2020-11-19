def justices_appointed_by(file, pres):
    just = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.split(',')
           
            if pres.lower() in data[2].lower(): 
                ans = data[0] + ' ' + data[1]
                just.append(ans)
                
    return just

