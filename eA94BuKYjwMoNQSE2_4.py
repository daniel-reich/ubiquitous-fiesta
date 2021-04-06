
def correct_signs(txt):
  l, op, r, *rest = txt.split()
  if   op == '<' and not (int(l) < int(r)): return False
  elif op == '>' and not (int(l) > int(r)): return False
  l = r
  
  while rest:
    op, r, *rest = rest
    if   op == '<' and not (int(l) < int(r)): return False
    elif op == '>' and not (int(l) > int(r)): return False
    l = r
    
  return True

