
def stem_plot(lst):
  stem_=[]
  leaf_=[]
  for i in range(len(lst)):
    if len(str(lst[i]))==1:
      stem_.append(0)
      leaf_.append(lst[i])
    else:
      stem_.append(int(str(lst[i])[:-1]))
      leaf_.append(int(str(lst[i])[-1]))
  stem_sort=stem_.copy()
  stem_sort.sort()
  leaf_sort=leaf_.copy()
  leaf_sort.sort()
  stem_uniq_sorted=list(dict.fromkeys(stem_sort))
  stem_uniq_sorted.sort()
  final_list=[]
  
  def get_index(stem_,stem_value):
    index_=[index for index, value in enumerate(stem_) if value == stem_value]
    return(index_)
  def _leaf_(leaf_,index_):
    list_leaf=[]
    for i in index_:
      list_leaf.append(leaf_[i])
    list_leaf.sort()
    return(list_leaf)
​
  for i in range(len(stem_uniq_sorted)):
    index_=get_index(stem_,stem_uniq_sorted[i])
    list_leaf=_leaf_(leaf_,index_)
    final_leaf=''
    for j in list_leaf:
      final_leaf+=str(j)
      final_leaf+=" "
    final_list.append(str(stem_uniq_sorted[i]) + " " + "|" + " " + final_leaf[:-1])
  return(final_list)

