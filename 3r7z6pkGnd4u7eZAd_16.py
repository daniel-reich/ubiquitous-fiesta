
def mark_maths(l):
    return str(round(sum(eval(n.replace('=', '==')) for n in l) / len(l) * 100)) + '%'

