
def valid(txt):
  if len(txt)  != 4 and len(txt)!=6: return False
  if not txt.isdigit(): return False
  return True

