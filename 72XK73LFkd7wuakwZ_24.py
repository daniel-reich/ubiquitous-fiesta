
def junction_or_self(n):
    control_list= list()
    for i in range(0, n):
        if n == (sum([int(j) for j in str(i)]) +i):
          control_list.append(i)
    return "Self" if (len(control_list)  == 0) else sorted(control_list, reverse=True)

