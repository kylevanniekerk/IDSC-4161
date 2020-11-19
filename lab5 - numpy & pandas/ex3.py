import numpy as np

def sales_for_store(file1, file2, store):
    arr1 = np.loadtxt(file1, dtype = np.int64, delimiter = ',')
    arr2 = np.loadtxt(file2)
    item1 = (arr1[0:,0:1]) * (arr2[0:1])
    item2 = (arr1[0:,1:2]) * (arr2[1:2])
    item3 = (arr1[0:,2:3]) * (arr2[2:3])
    item4 = (arr1[0:,3:4]) * (arr2[3:4])
    item5 = (arr1[0:,4:5]) * (arr2[4:5])
    if store == 1:
        sum1 = float(item1[0:1] + item2[0:1] + item3[0:1] + item4[0:1] + item5[0:1])
    if store == 2:
        sum1 = float(item1[1:2] + item2[1:2] + item3[1:2] + item4[1:2] + item5[1:2])
    if store == 3:
        sum1 = float(item1[2:3] + item2[2:3] + item3[2:3] + item4[2:3] + item5[2:3])
    return sum1