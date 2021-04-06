
def largest_even(lst):
  try: return list(set(i for i in lst if i%2==0))[-1]
  except: return -1

