def different_party(file):
    r = []
    d = []
    ans = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in  lines:
            data = line.split(',')
            if 'R' in data[2]:
                r.append(data)
                if 'D' in data[2]:
                    d.append(data[0])
        for i in range(0, len(r)):
            for item in d:
                if item in r[0]:
                    ans.append(r[1])
                
    return ans

