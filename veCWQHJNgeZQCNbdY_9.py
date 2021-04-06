
def root_digit(num):
 if int(num)<10:
   return num
 else:
    num=str(num)
    list1=[]
    for i in num:
      list1.append(int(i))
    return sum(list1) if sum(list1)<9 else root_digit(sum(list1))

