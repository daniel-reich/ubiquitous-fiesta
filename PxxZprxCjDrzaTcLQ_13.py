
def vowel_links(string):
  lst = string.split()
  vowels = ['a', 'e', 'i', 'o', 'u']
  for i in range(len(lst)):
    if i != len(lst)-1:
      print(i, lst[i][len(lst[i])-1], lst[i+1][0])
      if (lst[i][len(lst[i])-1] in vowels) and (lst[i+1][0] in vowels):
        return True
  return False

