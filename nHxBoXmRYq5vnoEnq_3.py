
def vowels(txt):
  return 0 if not txt else int(txt[0] in 'aeiou') + vowels(txt[1:])

