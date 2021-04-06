
def spartans_cipher(msg, n_Slide):
    r=[]
    txt=[]
    cipher =''
    c=4
    while(len(msg)>n_Slide*c):
        c+=1
    
    for row in range(n_Slide):
        for column in range(c):
            try:r.append(msg[column])
            except:r.append(' ')
        msg=msg[c:] 
        txt.append(r)     
        r=[]
    for column in range(c):
        for row in txt: cipher+=row[column]
​
    return ''.join(cipher).strip()

