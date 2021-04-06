
def is_vowel_sandwich(s):
  vowels = "aeiou"
  truth_list = []
  for x in s:
    if x in vowels:
      truth_list.append(True)
    else:
      truth_list.append(False)
  if truth_list == [False, True, False]:
    return True
  else:
    return False

