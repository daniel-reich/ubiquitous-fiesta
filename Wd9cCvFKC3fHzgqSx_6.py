
def num_split(num):
  string=str(num).replace('-','')
  lst=[int(string[i]+'0'*len(string[i+1:])) for i in range(len(string))]
  if num<0:
    return list(map(lambda x:-x,lst))
  return lst

