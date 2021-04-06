
def inclusive_list(start_num, end_num):
 allnumbers=[]
 if start_num >= end_num:
  allnumbers.append(start_num)
 else:
  for i in range(start_num, end_num+1):
   allnumbers.append(i)
 return(allnumbers)

