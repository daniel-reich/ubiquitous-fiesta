
def bowling(pins):
  total = 0
  frame = 0
  last = -1
​
  while frame < 10:
    pin = pins.pop(0)
    strike = pin == 10 and last != 0
    spare = pin + last == 10
    
    total += pin
    if spare:
      total += pins[0]
    if strike: 
      total += pins[0] + pins[1]
    
    frame += 1 if strike else 0.5
    last = pin if last < 0 and not strike else -1
  
  return total

