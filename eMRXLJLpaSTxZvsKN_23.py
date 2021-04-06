
import re
def is_ladder_safe(ldr):
  # 1st test width and integrity of each row, 2nd test column 1 for equal spacing
  return all(re.match(r'^#([ ]|#){3,}#', rung) and len(rung) == len(ldr[0]) for rung in ldr) \
    and bool(re.match(r'^ #([ ]{0,2}#)\1* $', [''.join(z) for z in list(zip(*ldr))][1]))

