
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
  n='0123456789'
  pin=[i for i in pin]
  if len(pin)!=4: return 'Invalid input.'
  for i in range(len(pin)):
    if pin[i] not in n: return 'Invalid input.'
    pin[i]=int(pin[i])+i
    if pin[i]>9: pin[i]-=10
  return [moves[i] for i in pin]

