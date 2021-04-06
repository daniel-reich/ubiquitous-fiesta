
def look_and_say(n):
    n=str(n)
    if len(n)%2==1:return "invalid"
    l=[n[i:i+2] for i in range(0,len(n),2)]
    return int("".join([i[1]*int(i[0]) for i in l]))

