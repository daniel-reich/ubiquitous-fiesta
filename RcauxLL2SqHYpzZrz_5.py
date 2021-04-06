
def true_equations(lst):
  z=[i.split("=") for i in lst]
  return  ["=".join(i) for i in z if int(eval(i[0]))==int(i[1])]

