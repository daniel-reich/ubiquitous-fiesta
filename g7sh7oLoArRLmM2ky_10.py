
def baconify(msg, mask=''):
  a = 'abcdefghijklmnopqrstuvwxyz. '
  if mask:
    msg = ''.join([i for i in msg if i.isalpha() or i in ' .'])
    binary = [decimal_to_binary(i) for i in msg.lower()]
    lst = []
    letters = ''.join([i for i in mask if i.isalpha()])
    lst = [letters[i:i+5] for i in range(0,len(letters),5)]
    if len(lst) == len(binary):
      lst = ''.join([binary_to_case(binary[i],lst[i]) for i in range(len(binary))])
    else:
      lst = ''.join([binary_to_case(binary[i],lst[i]) for i in range(len(binary))]+lst[len(binary):])
    ans = ''
    it = 0
    for i in mask:
      if i.isalpha():
        ans+=lst[it]
        it+=1
      else:
        ans+=i
    return ans
  else:
    msg = ''.join([i for i in msg if i.isalpha()])
    msg = [msg[i:i+5] for i in range(0,len(msg),5)]
    msg = [i for i in msg if len(i) == 5]
    msg = [a[binary_to_decimal(i)] for i in msg]
    return ''.join(msg)
  
def binary_to_decimal(s):
  b = ''.join(['0' if i.isupper() else '1' for i in s][::-1])
  if b == '11111':
    return 27
  elif b == '01111':
    return 26
  d = 0
  for i in range(len(b)):
    if b[i] == '1':
      d += 2**i
  return d
  
def decimal_to_binary(s):
  if s == '.':
    return '11110'
  elif s ==  ' ':
    return '11111'
  a = 'abcdefghijklmnopqrstuvwxyz'
  d = a.index(s)
  b = ''
  while d > 0:
    b += str(d%2)
    d = d//2
  b += '0'*(5-len(b)) 
  return b[::-1]
  
def binary_to_case(b,s):
  ret = ''
  it = 0
  for i in s:
    if i.isalpha():
      if b[it] == '0':
        ret+=i.upper()
      else:
        ret+=i.lower()
      it+=1
    else:
      ret+=i
  return ret

