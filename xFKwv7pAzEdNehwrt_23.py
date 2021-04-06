
def bracket_logic(xp):
  lib = {'(':')','[':']','{':'}','<':'>'}
  ob = "{[(<"
  cb = "]})>"
  br = []
  for i in xp:
    if i in ob:
      br.append(i)
    if i in cb:
      if lib[br[-1]] == i:
        br.pop(-1)
      else: return False
  return not len(br)

