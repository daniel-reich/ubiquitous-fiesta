
def describe_num(n):
  adj_lst = ["brilliant","exciting","fantastic","virtuous","heart-warming"]
  adj_lst+= ["tear-jerking","beautiful","exhilarating","emotional","inspiring"]
  
  adjs = " ".join(adj_lst[i] for i in range(10) if n%(i+1)==0)
  return "The most " + adjs + " number is " + str(n) + "!"

