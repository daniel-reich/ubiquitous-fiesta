
import re
translationMap = {
  "CV" : (1, 0),
  "CVV" : (1, 0, 2),
  "CVVV" : (1, 0, 2, 3),
  "CVC" : (1, 0, 2),
  "CVVC" : (1, 0, 2, 3),
  "CVVVC" : (1, 0, 2, 3, 4),
  "CCV" : (1, 2, 0),
  "CCVV" : (1, 2, 0, 3),
  "CCVVV" : (1, 2, 0, 3, 4),
  "CCVC" : (1, 2, 0, 3),
  "CCVVC" : (1, 2, 0, 3, 4),
  "CCVVVC" : (1, 2, 0, 3, 4 ,5)
}
​
def eadibitan(word):
  sylable = re.compile(r"(C{0,2}V{1,3}(?:C(?!V))?)+")
  wrdStruc = classifyLetters(word)
  sylables = []
  while wrdStruc:
    m = sylable.fullmatch(wrdStruc)
    if m is None:
      return
    s = m.group(1)
    sylables.append(s)
    wrdStruc = wrdStruc[:-len(s)]
  sylables.reverse()
  wrdParts = matchSplits(word, sylables)
  alteredWordParts = []
  for syl, frag in zip(sylables, wrdParts):
    if syl in translationMap:
      newFrag = []
      for idx in translationMap[syl]:
        newFrag.append(frag[idx])
      alteredWordParts.append("".join(newFrag))
    else:
      alteredWordParts.append(frag)
  return "".join(alteredWordParts)
    
def matchSplits(s, lst):
  parts = []
  for split in lst:
    parts.append(s[:len(split)])
    s =  s[len(split):]
  return parts
  
def classifyLetters(s):
  vowels = "aeiou"
  t = ['Y' if c == 'y' else 'V' if c in vowels else 'C' for c in s]
  for i, c in enumerate(t):
    if c == 'Y':
      if i + 1 < len(t):
        t[i] = 'C' if t[i+1] == 'V' else 'V'
      else:
        t[i] = 'V'
  return "".join(t)

