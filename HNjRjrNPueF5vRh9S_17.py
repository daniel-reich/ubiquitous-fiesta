
def hamming_code(message):
  ans=''
  for i in message:
    a=str(format(ord(i),'08b'))
    for j in a:
      ans+=j*3
  return ans

