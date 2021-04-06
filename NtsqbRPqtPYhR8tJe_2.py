
def blocks(step):
  if step <= 0:
    return 0
  if step == 1:
    return 5
  return (5+step) + blocks(step-1)

