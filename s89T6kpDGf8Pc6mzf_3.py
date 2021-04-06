
def seven_segment(txt):
  d = {
  "0": "abcdef",
  "1": "bc",
  "2": "abdeg",
  "3": "abcdg",
  "4": "bcfg",
  "5": "acdfg",
  "6": "acdefg",
  "7": "abc",
  "8": "abcdefg",
  "9": "abcfg"
  }
  return [sorted([c for c in d[txt[i]] if c not in d[txt[i+1]]]+[c.upper() for c in d[txt[i+1]] if c not in d[txt[i]]], key=str.lower) for i in range(len(txt)-1)]

