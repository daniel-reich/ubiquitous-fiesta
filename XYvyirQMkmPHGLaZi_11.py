
def boom_intensity(n):
    if n < 2:
        return 'b%sm'%('o'*2)
    else:
        return 'B'+(('O'*n+'M')if not(n%5) else('o'*n+'m')) +'!'*(not n%2)

