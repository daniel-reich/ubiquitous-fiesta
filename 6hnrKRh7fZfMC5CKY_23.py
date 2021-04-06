
def look_and_say(n):
    n = str(n)
    return int("".join(d[-1]*int(d[0]) for d in [n[i:i+2] for i in 
    range(0,len(n)-1,2)])) if len(n)%2==0 else "invalid"

