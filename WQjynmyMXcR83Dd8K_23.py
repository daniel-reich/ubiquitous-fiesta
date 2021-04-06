
def number_of_swaps(lst):
  swap = 0
  temp = 0
  while lst!=sorted(lst):
    for i in range(len(lst)-1):
      if lst[i]>lst[i+1]:
        temp=lst[i]
        lst[i]=lst[i+1]
        lst[i+1]=temp   
        swap+=1
  return swap

