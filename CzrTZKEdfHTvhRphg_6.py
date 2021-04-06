
def mixed_number(frac):
  separate=frac.split("/")
  factors=[no for no in range(1,int(separate[1])+1) if int(separate[0])%no==0 and int(separate[1])%no==0]
  if int(separate[0])==0:
    return "0"
  elif abs(int(separate[0]))<int(separate[1]):
    return str(int(separate[0])//max(factors)) +"/" +str(int(separate[1])//max(factors))
  else:
    wholeno=int(int(separate[0])/int(separate[1]))
    if wholeno*int(separate[1])==int(separate[0]):
      return str(wholeno)
    return str(wholeno) + " " +str((abs(int(separate[0]))-abs(wholeno)*int(separate[1]))//max(factors)) +"/" +str(int(separate[1])//max(factors))

