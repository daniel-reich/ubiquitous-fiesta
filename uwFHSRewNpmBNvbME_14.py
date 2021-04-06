
def same_vowel_group(w):
  vowels = 'aeiou'
  target = set([i for i in w[0] if i in vowels])
  print(target)
  new_word = []
  output = [w[0]]
  for i in w[1:]:
    new_word = []
    for l in i:
      if l in vowels:
        new_word.append(l)
        print(set(new_word))
    if set(new_word) == target:
      output.append(i)
  return output

