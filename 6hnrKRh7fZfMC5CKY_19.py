
def look_and_say(n):
  if len(str(n)) % 2 != 0:
    return "invalid"
    
  arr = []
  for i in range(0,len(str(n)),2):
    arr.append(str(n)[i:i+2])
  
  out = ""
  for x in arr:
    out += x[-1]*int(x[0])
  return int(out)

