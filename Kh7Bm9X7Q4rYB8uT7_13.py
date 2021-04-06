
def is_vowel_sandwich(s):
  return (True if len(s) == 3 and (s[0] not in "aeiouAEIOU" and s[2] not in "aeiouAEIOU") and (s[1] in "aeiouAEIOU") else False)

