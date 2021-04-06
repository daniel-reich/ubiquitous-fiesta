
def calculate_score(games):
  ls = ["R", "S", "P"]
  lst = [0 if x==y else [1, -1][x==ls[ls.index(y)-1]] for x,y in games]
  return "Tie" if sum(lst)==0 else ["Abigail", "Benson"][sum(lst)>0]

