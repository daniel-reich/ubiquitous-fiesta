
def josephus(n, i):
    circle = [str(o + 1) for o in range(n)]
    current_pop_pos = i - 1
    while len(circle) != 1:
        try:
            circle.pop(current_pop_pos)
            current_pop_pos += i - 1
        except:
            current_pop_pos = current_pop_pos - len(circle) 
    return int(circle[0])

