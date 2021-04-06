
def is_vowel_sandwich(s):
  vowels = ['a','e', 'i','o', 'u']
  if len(s) == 3:
    try:
      assert s[1] in vowels
      assert s[0] not in vowels
      assert s[-1] not in vowels
      return True
    except AssertionError:
      return False
  else:
    return False

