
def possible_path(lst):
  if lst[0]=="H":
    return all(y%2==0 for y,x in enumerate(lst) if x=="H") and all(y%2==1 for y,x in enumerate(lst) if str(x).isdigit())
  else:
    return all(y%2==0 for y,x in enumerate(lst) if str(x).isdigit()) and all(y%2==1 for y,x in enumerate(lst) if x=="H")

