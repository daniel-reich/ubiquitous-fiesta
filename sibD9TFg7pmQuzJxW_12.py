
def stem_plot(lst):
  lst = sorted(lst)
  #print(lst)
  dic = {}
  for i in lst : 
    if i <= 9 :
      if "0" not in dic :
        dic["0"] = []
        dic["0"].append(i)
      else : 
        dic["0"].append(i)
    elif i > 9 : 
      temp_cut = str(i)[:len(str(i))-1]
      if temp_cut not in dic :
        dic[temp_cut] = []
        dic[temp_cut].append(str(i)[-1])
      else : 
        dic[temp_cut].append(str(i)[-1])
  ans = []
  k = []
  for js in dic :
    k.append(int(js))
  k = list(map(str,sorted(list(map(int,k)))))
  for j in k :
    print(j)
    temp_str = ""
    temp_str += j + " |"
    for k in dic[j] :
      temp_str += " "+ str(k)
    ans.append(temp_str)
  return ans

