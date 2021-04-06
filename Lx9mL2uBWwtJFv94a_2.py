
def checker_board(n, el1, el2):
  gen = lambda n,a,b: n//2*[a,b]+n%2*[a]
  return "invalid" if el1==el2 else gen(n,gen(n,el1,el2),gen(n,el2,el1))

