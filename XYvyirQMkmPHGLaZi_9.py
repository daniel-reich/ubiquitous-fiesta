
def boom_intensity(n):
    if n < 2: 
        return 'boom'
    else:
        base = 'B'+n*'o'+'m'
        if n%2==0:
            base = base+'!'
        if n%5 ==0:
            base = base.upper()
    return base

