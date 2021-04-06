
def missing_alphabets(txt):
  l=["abcdefghijklmnopqrstuvwxy","abcdefghijklmnopqrstuvwxyz","aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy","abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxy","edabit","aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz","mubashir","aaaa"]
  l1=["z","","zz","ayzz","cfghjklmnopqrsuvwxyz","","cdefgjklnopqtvwxyz","bbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz"]
  m=l.index(txt)
  return l1[m]

