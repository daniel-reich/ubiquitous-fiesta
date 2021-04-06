
def get_missing_letters(s):
  missing = "";
  for i in range(26):
    if s.count(chr(97+i)) == 0:
      missing += chr(97+i);
  return missing;

