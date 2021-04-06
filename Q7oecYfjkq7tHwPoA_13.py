
def climb(stamina, obs):
    s=[int(abs(obs[i+1]-obs[i])+.9)*(1+1*(obs[i+1]>obs[i])) for i in range(len(obs)-1)]
    for i in range(len(s)):
        stamina-=s[i]
        if stamina<0:
            return i
    return i+1

