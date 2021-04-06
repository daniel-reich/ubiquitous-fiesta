
import sys
sys.setrecursionlimit(3000)
def sum_numbers(n):
  if n==0: return 0
  else: return n+sum_numbers(n-1)

