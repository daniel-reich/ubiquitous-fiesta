
def makeBox(n):
  return [str('#'*n)]+ ["#" + str(' '*(n-2)) + '#'] * (n-2) + [str('#'*n)] if n>1 else ['#']

