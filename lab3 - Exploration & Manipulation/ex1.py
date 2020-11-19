wordlist = [2]

def is_sorted(wordlist):
    flag = bool(1)
    i = 1
    while i < len(wordlist):
        if (wordlist[i] < wordlist[i - 1]):
            flag = bool(0)
        i += 1
    return flag
        
print('{0}'.format(is_sorted(wordlist))) 
    

