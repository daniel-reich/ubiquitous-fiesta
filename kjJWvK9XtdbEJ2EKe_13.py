
def sort_array(lst):
  lst_srt=[]
  for i in range(len(lst)):
    lst_srt.append(min(lst))
    lst.remove(min(lst))
  return(lst_srt)

