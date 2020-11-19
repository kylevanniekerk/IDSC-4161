import pandas as pd

def interpolated_median(file):
    grades = pd.read_csv(file, header = None)
    gpa = {'A':4.0, 'A-':3.67, 'B+':3.33, 'B':3.0, 'B-':2.67, 'C+':2.33,
           'C':2.00, 'C-':1.67, 'D+':1.33, 'D':1.0, 'D-':0.67, 'F': 0.0}
    grades['i'] = grades.apply(gpa.get)
    grades['med'] = grades.number.median()
    grades['l'] = grades.size
    lastgrades = pd.DataFrame(grades[grades['i'] < grades['med']])
    grades['low'] = lastgrades['i'].size
    egrades = pd.DataFrame(grades[grades['i'] == grades['med']])
    grades['e'] = egrades.size
    grades['tot'] = grades['med'] - 0.167 + (((0.5 * grades['l']) - grades['low']) / grades['e']) * 0.33
    totgpa = grades.iloc[0.6]
    return round(totgpa, 3)

