
def censor(string):
    t=''
    for i in string.split():
       if len(i)>4:
           t=t+('*'*len(i))+' '
       else:
           t=t+i+' '
    return t.rstrip()

