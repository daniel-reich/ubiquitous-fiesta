
def josephus(number, interval):
    persons = [i+1 for i in range(number)]
    temps = persons
    pos = 0
    while len(temps) > 1:
        pos_to_kill = (pos+interval-1)%number
        next_val = temps[(pos_to_kill+1)%number]
        temps.pop(pos_to_kill)
        pos = temps.index(next_val)
        number = number -1
    
    return temps[0]

