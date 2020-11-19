

lst = ['Bob', 'Alice', 'Jerry', 'Jerry', 'Nathan', 'Alice']

def duplicate_names(lst):
    ans = []
    for elem in lst:
        if lst.count(elem) > 1:
            ans.append(elem)
    ans = list(dict.fromkeys(ans))
    return ans
            