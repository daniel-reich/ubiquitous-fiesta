
def empty_sq(step):
  return (step*2-2)*4 + empty_sq(step-1) if step>1 else 0

