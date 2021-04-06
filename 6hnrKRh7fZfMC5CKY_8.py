
def look_and_say(n):
  s=str(n)
  if len(s)%2:
    return "invalid"
  return int("".join(int(x)*y for x,y in zip(s[::2],s[1::2])))

