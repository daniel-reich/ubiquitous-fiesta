
def arithmetic_operation(n):
  n1, op, n2 = n.split()
  n1, n2 = int(n1), int(n2)
  if op == "+": return n1 + n2
  if op == "-": return n1 - n2
  if op == "*": return n1 * n2
  return n1 // n2 if n2 else -1

