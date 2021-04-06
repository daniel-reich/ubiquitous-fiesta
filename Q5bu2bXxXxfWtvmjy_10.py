
def missing_letter(txt):
  ascii = [ord(x) for x in txt]
  letter = [chr(x) for x in range(min(ascii), max(ascii)) if x not in ascii]
  return "No Missing Letter" if len(letter) == 0 else letter[0]

