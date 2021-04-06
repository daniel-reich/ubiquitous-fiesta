
def look_and_say(n):
    if len(str(n))%2!=0:
        return 'invalid'
    else:
        x=[str(n)[i:i+2] for i in range(0,len(str(n)),2)]
        y=int(''.join([i[1]*int(i[0]) for i in x]))
        return y

