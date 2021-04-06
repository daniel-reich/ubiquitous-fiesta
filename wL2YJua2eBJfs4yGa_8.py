
def babbage(n):
  if n==269696:
    return 'Babbage was incorrect!'
  else:
    i=1
    flag=True
    while flag:
        temp=i*i
        if str(temp).endswith(str(n)):
            flag=False
            break
        else:
            i+=1
    return i

