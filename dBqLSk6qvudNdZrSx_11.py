
def is_boiling(temp):
  if int(temp[:len(temp)-1]) >= 100 and temp[-1] == 'C':return True
  elif int(temp[:len(temp)-1]) >= 212 and temp[-1] == 'F':return True
  else:return False

