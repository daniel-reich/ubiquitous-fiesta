
txt = 'abcdefghijklmnopqrstuvwxyz'
nums = '0123456789'
​
def challenge1(txt):
  return txt[0:5]
print(challenge1(txt))
  
def challenge2(txt):
  return txt[-5::]
print(challenge2(txt))
​
def challenge3(txt):
    return txt[::-1]
print(challenge3(txt))
  
def challenge4(txt):
  return txt[::-1][-6::]
print(challenge4(txt))
def challenge5(txt):
  return txt[-7::2]
print(challenge5(txt))

