
def choose_fuse(fuses, current):
    c = current[:-1]
    new_list = []
    for f in fuses:
        new_list.append(float(f[:-1]))
    
    new_list.sort()
​
    for i in new_list:
        if float(c) <= i:
            return str(int(i)) + "V"

