import pandas as pd

def years_w_no_appointments(file):
    just = pd.read_csv(file, header = None)
    x = pd.Series(range(1789,2010))
    years = x[x.isin(just[4]) == False]
    return years
