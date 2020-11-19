import numpy as np 

def rankings_for(file, uni):
    arr = np.loadtxt(file, dtype = str, delimiter = ',')
    lst = []
    for i in arr: 
        x = np.isin(arr[0,i], uni)
        y = np.isin(arr[1,i], uni)
        z = np.isin(arr[2,i], uni)
        if x == True:
            recx = arr[0,0]
            lst.append(recx)
        if y == True:
            recy = arr[1,0]
            lst.append(recy)
        if z == True:
            recz = arr[2,0]
            lst.append(recz)
            
    return np.array(lst)
