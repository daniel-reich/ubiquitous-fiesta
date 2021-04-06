
import re
def is_long_pressed(original, typed):
  opieces = [m.group(0) for m in re.finditer(r'(.)\1*', original)]
  tpieces = [m.group(0) for m in re.finditer(r'(.)\1*', typed)]
  
  return len(opieces)==len(tpieces) and \
      all(op[0]==tp[0] and len(op)<=len(tp) for op,tp in zip(opieces,tpieces))

