
def chunkify(lst, size):
 output=[]
 i=0
 new_list=[]
 n=0
 while i < len(lst):
  output.append([])
  #print(output)
  for k in range(0,size):
   if i < len(lst):
    output[n].append(lst[i])
    i+=1
   else:
    break
  n+=1
 return output

