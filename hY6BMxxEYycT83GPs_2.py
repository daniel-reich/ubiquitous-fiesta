
def multiply_by_11(num):
  rst = num[-1]
  ten = [None]*len(num)
  ten[-1] = 0
  for i in range(len(num)-1):
    sm = int(num[-(i+1)])+int(num[-(i+2)])
    if sm+ten[-(i+1)] < 10:
      ten[-(i+2)] = 0
      rst = str(int(str(sm)[0])+ten[-(i+1)])+rst  
    if sm+ten[-(i+1)] == 10:  
      ten[-(i+2)] = 1
      rst = str(0)+rst
    if sm+ten[-(i+1)] > 10:
      ten[-(i+2)] = 1
      rst = str(int(str(sm)[1])+ten[-(i+1)])+rst  
  if len(num)<3:
    final_rst = str(int(num[0])+ten[-(len(num))])+rst
  else:
    final_rst = str(int(num[0])+ten[-(len(num)-1)])+rst
  return final_rst

