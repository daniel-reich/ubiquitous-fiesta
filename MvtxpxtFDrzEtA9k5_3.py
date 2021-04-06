
def palindrome_descendant(num):
  num = str(num) 
  while len(num) > 1:
    if (num == num[::-1]): return True
    x=[]
    num = list(map(int,num))
    for i in range(1,len(num),2):
      x.append(num[i-1] + num[i])   
    if len(num)%2 != 0 : 
      x.append(num[-1])       
    num=x
    num = str(int("".join(map(str, num))))
  return False

