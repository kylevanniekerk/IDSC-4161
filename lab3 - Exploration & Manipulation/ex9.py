import numpy as np 
def correl(file, col1, col2):
    x = []
    y = []
    r = float(0)
    with open(file, 'r') as f:
        lines = f.read().strip().split(" ")
        data1 = lines[1:1693]
        line = f.readline()
        data = line.split(',')
        for i in data:
            if col1 in range[data]:
                for l in range(1,len(data1)):
                    x.append(l)
            elif col2 in range[data]:
                for l in range(1,len(data1)):
                    y.append(l)
                
        r = np.corrcoef(x,y)
    return r


