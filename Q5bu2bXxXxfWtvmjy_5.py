
def missing_letter(txt):
  miss = [chr(n) for n in range(ord(txt[0]),ord(txt[-1])) if chr(n) not in txt]
  if miss == []:
    return "No Missing Letter"
  return miss[0]

