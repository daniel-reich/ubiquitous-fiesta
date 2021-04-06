
def c_cipher(msg, keyword):
  if ' ' in msg:
    n = len(keyword)
    msg = [ch.lower() for ch in msg if ch.isalnum()]
    msg = [msg[i:i+n] for i in range(0,len(msg),n)]
    if len(msg[-1]) < n:
      msg[-1] += ['x'] * (n-len(msg[-1]))
    msg = zip(*msg)
    msg = [''.join(i) for i in msg]
​
    lst = []
    for i in range(n):
      lst.append([keyword[i],msg[i]])
    lst = sorted(lst,key=lambda x: x[0])
    
    coded = ''.join(''.join(lst[i][1] for i in range(n)))
    return coded
  
  else:
    n = len(msg)//len(keyword)
    sort_key = sorted(list(keyword))
    msg = [msg[i:i+n] for i in range(0,len(msg),n)]
    
    lst = []
    for i in range(len(keyword)):
      lst.append([sort_key[i],msg[i]])
    lst = sorted(lst,key=lambda x: keyword.index(x[0]))
    lst = zip(*[lst[i][1] for i in range(len(lst))])
​
    decoded = ''.join(''.join(i) for i in lst)
    return decoded

