
def encrypt(key, message):
  dic = {key[i+1]:key[i] for i in range(0,len(key),2)}
  dic.update({v:k for k,v in dic.items() if v not in dic})
  return ''.join(dic[c] if c in dic else c for c in message)

