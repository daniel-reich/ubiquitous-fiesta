
def compress(chars):
    chars = ''.join(chars)
    ans=''
    for i,char in enumerate(chars):
        if char!=chars[i-1]:ans+=" "+char
        else:ans+=char
    return ''.join(list(map(lambda x:x[0] + str(x.count(x[0])) if x.count(x[0]) !=1 else x[0] ,ans.strip().split(" "))))

