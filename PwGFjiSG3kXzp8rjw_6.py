
def chatroom_status(users):
    l = len(users)
    if l==0:
        return 'no one online'
    elif l==1:
        return '%s online'%users[0]
    elif l==2:
        return '%s and %s online'%(users[0],users[1])
    else:
        return'%s, %s and %d more online'%(users[0],users[1],len(users)-2)

