
def vowels(string):
  if len(string) == 0: return 0;
  return 1 + vowels(string[1:]) if string[0] in "aeiouAEIOU" else 0 + vowels(string[1:]);

