
def is_ladder_safe(ldr):
  gap,rung = ldr[0],'#'*len(ldr[0])
  pattern = ['a' if i==rung else 'b' if i==gap else 'c' for i in ldr]
  return len(ldr[0])>4 and pattern==pattern[::-1] and 'bbb' not in ''.join(pattern)

