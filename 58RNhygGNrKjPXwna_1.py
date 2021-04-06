
def longest_nonrepeating_substring(txt):
  lst = [txt[i:j] for i in range(len(txt)) for j in range(i+1,len(txt)+1)]
  lst = [i for i in lst if len(set(i))==len(i)]
  return max(lst,key=len)

