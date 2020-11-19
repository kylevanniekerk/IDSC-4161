import statistics as stat

lst = [ 'A−' , 'B ' , 'C ' , 'A ' , 'C ' , 'A ' , 'B ' , 'C−' , 'C+' , 'B−' ,'B−' , 'A−' , 'B ' , 'B+' , 'C−' , 'C+' , 'C ' , 'B−' , 'A ' , 'C ' ,'C ' , 'B−' , 'A ' , 'C−' , 'C ' ]

def interpolated_median(lst):
    grades = []
    for i in lst:
        if i == 'A':
            grades.append(4.0)
        if i == 'A-':
            grades.append(3.67)
        if i == 'B+':
            grades.append(3.33)
        if i == 'B':
            grades.append(3.0)
        if i == 'B-':
            grades.append(2.67)
        if i == 'C+':
            grades.append(2.33)
        if i == 'C':
            grades.append(2.0)
        if i == 'C-':
            grades.append(1.67)
    m = stat.median(grades)
    n = len(grades)
    n1 = 0
    n2 = 0
    for itm in grades:
        if itm < m:
            n1 += 1
        if itm == m:
            n2 += 1
    if n2 == 0:
        im = m 
    else:
        im = m - 0.167 + (((0.5 * n) - n1)/n2) * 0.333
    return im
        

