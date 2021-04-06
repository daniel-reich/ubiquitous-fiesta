
def blocks(step):
  return sum(([5]+[7+i for i in range(step-1)])[:step])

