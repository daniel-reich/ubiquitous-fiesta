
import re
def arithmetic_operation(n):
  op = re.search(r'(?<= ).*(?= )', n).group()
  a, b = map(int, n.split(" " + op + " "))
  if op == '+': return a + b
  if op == '-': return a - b
  if op == '*': return a * b
  if op == '//': return a // b if b else -1

