
def club_entry(word):
  alphabet=['a',  'b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n',  'o',  'p',  'q',  'r',  's',  't',  'u',  'v',  'w',  'x',  'y',  'z']
  repalpha=''
  temp=''
  for a in word:
    if temp == a:
      repalpha=a
    temp = a
  varint = (alphabet.index(repalpha)+1)*4
  return varint

