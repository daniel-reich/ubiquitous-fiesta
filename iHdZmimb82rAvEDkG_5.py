
def bitwise_index(lst):
  lst_even=list(filter(lambda x:x%2==0,lst))
  if len(lst_even)==0:
    return "No even integer found!"
  else:
    a=lst.index(max(lst_even))
    if a%2==0:
      return {'@even index {}'.format(a):max(lst_even)}
    else:
      return {'@odd index {}'.format(a):max(lst_even)}

