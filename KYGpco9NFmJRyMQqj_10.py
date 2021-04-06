
def min_removals(txt1, txt2):
  txt1_1=set(txt1)
  txt2_2=set(txt2)
  return len(txt1_1^txt2_2)

