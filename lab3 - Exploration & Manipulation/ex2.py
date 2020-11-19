

def is_sorted(filename):
    flag = bool(1)
    with open(filename, 'r') as f:
        for line in f:
            states = [line.strip() for line in f]
            i = 1
            while i < len(states):
                if (states[i] < states[i - 1]):
                    flag = bool(0)
                i += 1
    return list(filename)
    
