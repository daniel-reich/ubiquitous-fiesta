
def look_and_say(n):
  return int("".join(str(n)[i+1] * int(str(n)[i]) for i in range(0, len(str(n)), 2))) if len(str(n)) % 2 == 0 else "invalid"

