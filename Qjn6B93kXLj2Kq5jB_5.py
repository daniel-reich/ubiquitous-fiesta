
def simplify_frac(string):
    return ["{}/{}".format(int(int(string.split('/')[0])/[e for e in range(1,int(string.split('/')[0])+1,1) if int(string.split('/')[0]) % e == 0][i]),int(int(string.split('/')[1])/[e for e in range(1,int(string.split('/')[0])+1,1) if int(string.split('/')[0]) % e == 0][i])) for i in range(-1,-len([e for e in range(1,int(string.split('/')[0])+1,1) if int(string.split('/')[0]) % e == 0])-1,-1) if [e for e in range(1,int(string.split('/')[0])+1,1) if int(string.split('/')[0]) % e == 0][i] in [e for e in range(1,int(string.split('/')[1])+1,1) if int(string.split('/')[1]) % e == 0]][0]

