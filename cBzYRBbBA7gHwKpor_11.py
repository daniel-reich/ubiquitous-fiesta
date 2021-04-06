
import re
def secret_password(message):
    if len(re.sub(r'[a-z]','',message))>0 or len(message)!=9:return "BANG! BANG! BANG!"
    res = [message[i:i+3] for i in range(0,9,3)]
    res[0] = str(ord(res[0][0])-96)+res[0][1]+str(ord(res[0][2])-96)
    res[1] = res[1][::-1]
    res[2]= ''.join(list(map(lambda x:chr(ord(x)+1) if ord(x)+1-96<27 else chr(ord(x)+1-26), list(res[2]))))
    return  res[1]+res[2]+res[0]

