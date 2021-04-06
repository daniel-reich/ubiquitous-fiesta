
def pirates_killed(gold, tolerance):
  ineq = [max(gold) - i for i in gold]
  return any(ineq[i] > tolerance[i] for i in range(len(tolerance)))

