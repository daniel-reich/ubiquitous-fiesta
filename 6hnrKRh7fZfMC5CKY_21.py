
def look_and_say(n):
  if len(str(n)) % 2 != 0:
    return "invalid"
  output = ""
  for index, element in enumerate(str(n)):
    if (index + 1) % 2 != 0:
      qtt = element
    else:
      output += element * int(qtt)  
  return int(output)

