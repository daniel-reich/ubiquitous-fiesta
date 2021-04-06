
def clean_up_list(lst):
  arr = [int(x) for x in lst if int(x)%2==0]
  cat = [int(x) for x in lst if int(x)%2==1]
  return [arr,cat];

