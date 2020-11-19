

def mpg(file): 
    dic = {'Accord' : 0, 'Camry' : 0, 'Mustang' : 0, 'Prius' : 0, 'Sebring' : 0}
    name = []
    count = 0
    with open(file, 'r') as f:
        lines = f.readlines()
        for line  in lines:
            data = line.split(',')
            name.append(data)
        for i in name[0]:
            if name[0] == 'Accord':
                count += 1
                dic['Accord'] += (100/name[1])/count
            if name[0] == 'Camry':
                count += 1
                dic['Camry'] += (100/name[1])/count
            if name[0] == 'Mustang':
                count += 1
                dic['Mustang'] += (100/name[1])/count
            if name[0] == 'Prius':
                count += 1
                dic['Prius'] += (100/name[1])/count
            if name[0] == 'Sebring':
                count += 1
                dic['Sebring'] += (100/name[1])/count
    return dic
        
            

