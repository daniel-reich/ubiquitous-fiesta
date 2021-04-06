
def look_and_say(n):
  if len(str(n)) % 2 == 1:
    return 'invalid'
  
  return int("".join([str(n)[i:i+2][1] * int(str(n)[i:i+2][0]) for i in range(len(str(n)))[::2]]))

