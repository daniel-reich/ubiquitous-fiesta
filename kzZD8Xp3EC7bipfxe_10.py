
def worded_math(equ):
  
  def txt_to_num(txt):
    if txt.lower() == "zero": return 0
    if txt.lower() == "one": return 1
    if txt.lower() == "two": return 2
  
  nums = ["Zero", "One", "Two"]
  words = equ.split()
  
  lhs = txt_to_num(words[0])
  op = words[1]
  rhs = txt_to_num(words[2])
  
  if op.lower() == "plus": return nums[lhs + rhs]
  return nums[lhs - rhs]

