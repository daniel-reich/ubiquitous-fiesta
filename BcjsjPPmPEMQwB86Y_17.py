
def get_vowel_substrings(string):
  solution = []
  vowels = ['a','e','i','o','u']
  for num in range(len(string)):
    for digit in range(num+1, len(string)+1):
      if string[num:digit][0] in vowels and string[num:digit][-1] in vowels:
        solution.append(string[num:digit])
  return sorted(set(solution))
​
def get_consonant_substrings(string):
  solution = []
  consonants = [
  'b','c','d','f','g','h','j',
  'k','l','m','n','p','q','r','s','t','v','x','z','w','y'
      ]
  for num in range(len(string)):
    for digit in range(num+1, len(string)+1):
      if string[num:digit][0] in consonants and string[num:digit][-1] in consonants:
        solution.append(string[num:digit])
  return sorted(set(solution))

