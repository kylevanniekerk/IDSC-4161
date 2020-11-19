def multiples_diff(file, n):
    diff = int(0)
    ammo = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip().split(" ")
            for i in data:
                ammo += i.split(',')
        for nums in range(0,len(ammo)):
            ammo[nums] = int(ammo[nums])
            
            
        x = int(0)
        y = int(0)
    
        for num in range(0, len(ammo)):
            if ammo[num] % n == 0:
                x += ammo[num]
                
            else:
                y += ammo[num]
               
        diff = abs(x - y)
    return diff
       