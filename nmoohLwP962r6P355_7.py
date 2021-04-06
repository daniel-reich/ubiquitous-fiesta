
def straight_digital(number):
    x = ''.join(
    n 
    for n in str(number) 
    if n.isdigit()
  )
    d = [
        int(j) - int(i)
        for i, j in zip(x, x[1:])
    ]
    if len(set(d)) > 1 or number < 100:
        return 'Not Straight'
    elif len(set(x)) == 1:
        return 'Trivial Straight'
    else:
        return d[0]

