
def sentence_primeness(txt):
  d={str(i):i for i in range(10)}
  d.update({chr(65+i):i+1 for i in range(26)})
  d.update({chr(97+i):i+1 for i in range(26)})
  txt=''.join(i if i.isalnum() else ' ' for i in txt).split()
  val=[sum(d[i] for i in word) for word in txt]
  sval=sum(val)
  if isprime(sval):return "Prime Sentence"
  for a,b in zip(txt,val):
    if isprime(sval-b):return 'Almost Prime Sentence ({})'.format(a)
  return "Composite Sentence"
  
def isprime(num):
  return num>1 and all([num%i for i in range(2,num//2+1)])

