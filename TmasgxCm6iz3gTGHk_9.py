
def min_length(lst, n):
  lst=[lst[i:j] for i in range(len(lst)) for j in range(i+1,len(lst)+1) if sum(lst[i:j])>n]
  return min([len(i) for i in lst] if lst!=[] else [-1])

