
def digital_cipher(message, key):
    key = list((str(key)*(len(message)//len(str(key))+1))[:len(message)])
    ans = list(map(lambda x:ord(x),list(message)))
    return  list(map(lambda x:int(x[0] )+ x[1]-96, list(zip(key,ans))))

