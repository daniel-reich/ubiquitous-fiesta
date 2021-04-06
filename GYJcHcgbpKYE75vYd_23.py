
def return_end_of_number(num):
  dic = {1:'-ST',2:'-ND',3:'-RD'}
  if num%100 in range(11,14) or num%10 not in dic:
    return str(num)+'-TH'
  return str(num)+dic[num%10]

