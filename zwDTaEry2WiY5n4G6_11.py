
def digital_vowel_ban(n, ban):
  name = {"0":"eo","1":"oe","2":"o","3":"e","4":"ou","5":"ie","6":"i","7":"e","8":"ei","9":"ie"}
  nban = "".join(d for d in str(n) if ban not in name[d])
  return int(nban) if nban else "Banned Number"

