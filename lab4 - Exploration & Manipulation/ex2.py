import collections
lst = [1.21, 1.82, 1.9, 1.31, 2.45, 2.2, 1.4, 2.74, 2.99, 2.38]

def classify_eggs(lst):
    ans = []
    small = 'Small: ' + str(len([itm for itm, count in collections.Counter(lst).items() if itm > 1.5 and itm < 1.75]))
    med = 'Medium: ' + str(len([itm for itm, count in collections.Counter(lst).items() if itm > 1.75 and itm < 2]))
    large = 'Large: ' + str(len([itm for itm, count in collections.Counter(lst).items() if itm > 2 and itm < 2.25]))
    exlar = 'Extra LArge: ' + str(len([itm for itm, count in collections.Counter(lst).items() if itm > 2.25 and itm < 2.5]))
    jumbo = 'Jumbo: ' + str(len([itm for itm, count in collections.Counter(lst).items() if itm > 2.5]))
    
    if len([itm for itm, count in collections.Counter(lst).items() if itm > 1.5 and itm < 1.75]) >= 1:
        ans.append(small)
    if len([itm for itm, count in collections.Counter(lst).items() if itm > 1.75 and itm < 2]) >= 1:
        ans.append(med)
    if len([itm for itm, count in collections.Counter(lst).items() if itm > 2 and itm < 2.25]) >= 1:
        ans.append(large)
    if len([itm for itm, count in collections.Counter(lst).items() if itm > 2.25 and itm < 2.5]) >= 1:
        ans.append(exlar)
    if len([itm for itm, count in collections.Counter(lst).items() if itm > 2.5]) >= 1:
        ans.append(jumbo)
    return ans 
            

