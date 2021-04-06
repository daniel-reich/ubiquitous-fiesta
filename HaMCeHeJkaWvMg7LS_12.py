
def sun_loungers(beach):
    beach='0'+beach+'0'
    beach=[i for i in beach]
    k=0
    for i in range(1,len(beach)-1):
        if beach[i-1]=='0' and beach[i+1]=='0' and beach[i]!='1':
            beach[i]='1'
            k+=1
    return k

