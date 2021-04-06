
def unique(lst):
  lst.sort()
  hlp=len(lst)-2
  for i in range(1,len(lst)-1):
    item_prev=lst[i-1]
    item_now=lst[i]
    item_next=lst[i+1]
    if(item_prev!=item_now and item_now!=item_next):
      return item_now
    if(i==hlp and item_now!=item_next):
      return item_next
    if(item_prev!=item_now and item_now==item_next and i==1):
      return item_prev

