
def look_and_say(n):
​
  if len(str(n)) % 2 :
    return 'invalid'
  else:
    n = [ str(n)[i:i+2] for i in range(0,len(str(n)),2)]
    n = [ int(t[0]) * t[-1] for t in n ]
    return int(''.join(n))

