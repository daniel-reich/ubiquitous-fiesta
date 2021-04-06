
def seq_level(lst):
  a = [lst[i+1] - lst[i] for i in range(len(lst)-1)]
  if a[0]==a[-1]:
    return "Linear"
  elif seq_level(a) == "Linear":
    return "Quadratic"
  elif seq_level(a) == "Quadratic":
    return "Cubic"

