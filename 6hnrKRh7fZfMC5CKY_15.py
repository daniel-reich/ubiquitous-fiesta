
def look_and_say(n):
    s = str(n)
    if len(s) % 2 != 0:
        return 'invalid'
    return int(''.join([f(s[i:i+2]) for i in range(0, len(s), 2)]))
    
def f(x):
    return int(x[0])*x[1]

