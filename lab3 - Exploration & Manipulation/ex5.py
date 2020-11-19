def starts_with(filename, pre):
    count = 0
    pre = str(pre)
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            words = line.lower()
            if words.lower().startswith(pre.lower()):
                count += 1
        return count

