
def look_and_say(n):
    if len(str(n))%2!=0:
        return "invalid"
    else:
        g = [str(n)[::2]]
        h= [str(n)[1::2]]
        j=""
        for i in range(len(g[0])):
            j+=(int(g[0][i]) * h[0][i])
    return int(j)

