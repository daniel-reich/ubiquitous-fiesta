
import itertools
​
def get_vowel_substrings(txt):
  found_singles = [x[0] for x in enumerate(txt) if x[1] in 'aeiou']
  found_pairs = list(itertools.combinations(found_singles, 2))
  out = [txt[x] for x in found_singles]
  out.extend([txt[x[0]:x[1] + 1] for x in found_pairs])
  return sorted(set(out))
​
def get_consonant_substrings(txt):
  found_singles = [x[0] for x in enumerate(txt) if x[1] not in 'aeiou']
  found_pairs = list(itertools.combinations(found_singles, 2))
  out = [txt[x] for x in found_singles]
  out.extend([txt[x[0]:x[1] + 1] for x in found_pairs])
  return sorted(set(out))

