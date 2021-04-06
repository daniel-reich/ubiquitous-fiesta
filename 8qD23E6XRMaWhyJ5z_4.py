
def happiness_number(s):
  smilie1 = s.count(":)")
  smilie2 = s.count("):")
  smilie3 = s.count(":(")
  smilie4 = s.count("(:")
  return (smilie1 - smilie2 - smilie3 + smilie4)

