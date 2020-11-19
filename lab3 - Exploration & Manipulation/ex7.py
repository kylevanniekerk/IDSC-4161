def states_w_n_justices(file1, file2, n):
    states = []
    ammo = []
    newcount = 0
    with open(file1, 'r') as f1:
        lines1 = f1.readlines()
        for line1 in lines1:
            data1 = line1.split(',')
            states.append(data1[1])
    with open(file2, 'r') as f2:
        lines2 = f2.readlines()
        for line2 in lines2:
            data2 = line2.split(',')
            ammo.append(data2[3])
        for i in ammo:
            count = ammo.count(i.lower())
            if n == count:
                newcount += 1
            elif n == 0:
                newcount == 19
    return newcount
                
                
                
                
                    
    
        
        

