
def is_good_match(lst):
  return "bad match" if len(lst)%2!=0 else [lst[i]+lst[i+1] for i in range(0,len(lst),2)]

