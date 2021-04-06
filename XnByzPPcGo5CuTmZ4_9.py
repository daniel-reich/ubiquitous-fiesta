
def kix_code(addr):
  
  lst = [i.split(" ") for i in addr.split(",")[1:]]
  post = [i for i in lst[0][-1]]
​
  if len(lst[0]) == 4:
    post = [i for i in lst[0][-2] + "-" + lst[0][-1]]
​
  for i in range(len(post)):
    if post[i] == "-" or post[i] == "/":
      post[i] = "X"
  
  return lst[1][1] + lst[1][2] + "".join(post).upper()

