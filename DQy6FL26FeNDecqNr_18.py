
def correct_stream(user, correct):
    l=[]
    x=len(user)
    y=0
    for i in range(x):
        if(sorted(user[i])==sorted(correct[i])):
            l.append(1)
        else:
            l.append(-1)
    return l

