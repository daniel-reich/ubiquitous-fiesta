
def encrypt(key, message):
  encrypted = ""
  for i in message:
    if i in key:
      if key.index(i)%2 == 0:
        encrypted += key[key.index(i)+1]
      else:
        encrypted += key[key.index(i)-1]
    else:
      encrypted += i
  return encrypted

