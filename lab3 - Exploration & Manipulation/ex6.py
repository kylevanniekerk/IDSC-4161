def appointed_by(file, pres):
    year = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.split(',')
            data[4] = int(data[4])
            if pres.lower() in data[2].lower():
                year.append(data[4])
                
    return min(year), max(year)


