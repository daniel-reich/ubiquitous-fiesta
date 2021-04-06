
def get_items_at(arr, par):
  
  lth = len(arr)
  def r(arr,idx,lth):
    if (-1*idx)==lth+1: 
      return []
      
    else:
      arr2 = []
      if idx%2==0 and par=='even':
        arr2.append(arr[idx])
        arr2.extend(r(arr,idx-1,lth))
      elif idx%2!=0 and par=='odd':
        arr2.append(arr[idx])
        arr2.extend(r(arr,idx-1,lth))
      else:
        arr2.extend(r(arr,idx-1,lth))
      return arr2
  return r(arr,-1,lth)[::-1]

