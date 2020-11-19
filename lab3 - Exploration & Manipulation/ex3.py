def state_density(filename, state):
    density = float(0)
    with open(filename, 'r') as f:
        line = f.readline()
        for line in f: 
            data = line.split(',')
            data[2] = int(data[2])
            data[3] = int(data[3])
            if state == data[0]:
                density = data[3]/data[2]
    return density

