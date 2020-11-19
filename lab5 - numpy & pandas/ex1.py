import numpy as np

def miles_between(file, f_id, t_id):
    arr = np.loadtxt(file, dtype = np.int64, delimiter = ',')
    
    return arr[f_id:t_id]

