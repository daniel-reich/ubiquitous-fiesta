
def reverse(txt):
  return "".join([txt[letter].upper() if txt[letter].islower() else txt[letter].lower() for letter in range(len(txt)-1,-1,-1) ])

