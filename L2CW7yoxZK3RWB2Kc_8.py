
def crypt(key,msglen):
    key1 =[y for (x,y) in 
      sorted([(lett,indx) for indx,lett in enumerate(key)])]
    return [(i, len(key)* (i//len(key)) + key1[i%len(key)]) 
      for i in range(0,msglen)]
​
def nico_cipher(message, key):
    if len(message)%len(key) != 0:
        message = message + (len(key) - len(message)%len(key)
        ) * ' '
    return ''.join([ message[y] 
        for (x,y) in crypt(key,len(message)) ])

