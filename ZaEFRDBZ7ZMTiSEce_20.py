
def find_nemo(arr):
  c=1
  for i in range(len(arr)):
    if arr[i]==" ":
      c=c+1
    if arr[i]=="N" and arr[i+1]=="e" and arr[i+2]=="m" and arr[i+3]=="o" and arr[i+4]==" ":
      return("I found Nemo at "+str(c)+"!")
  return "I can't find Nemo :("

