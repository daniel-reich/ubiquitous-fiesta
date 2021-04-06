
def is_correct_aliases(names, aliases):
    
    q = [a.split() for a in aliases]
    q = [q[i][0][0] == q[i][1][0] == names[i][0] for i in range(len(q))]
​
    return False not in q

