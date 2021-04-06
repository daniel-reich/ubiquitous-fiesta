
def seven_segment(txt):
  # represent each digit as a binary string of length 7 
  digits = [bin(sum(2**(ord(c) - 97) for c in w))[2:].zfill(7) for w in  ['abcdef', 'bc', 'abdeg', 'abcdg', 'bcfg', 'acdfg', 'acdefg', 'abc', 'abcdefg', 'abcfg']]
  seg_trans = []
  for i, tran in enumerate([(int(f), int(t)) for f, t in zip(txt, txt[1:])]):
    # get binary reprentation of transition from -> to
    fr, to = digits[int(tran[0])], digits[int(tran[1])]
    # get upper or lower case character representing segment transitioned 
    seg = [chr(71-i) if fr[i] < to[i] else chr(103-i) for i in range(6, -1,-1) if fr[i] != to[i]]
    # case insensitive segments sort
    seg_trans.append(sorted(seg, key=str.upper))
  return seg_trans

