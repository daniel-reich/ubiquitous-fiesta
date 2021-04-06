
def alternate_sort(lst):
  return sum((list((a,b)) for a,b in 
              zip(sorted([e for e in lst if type(e)==int]),
                  sorted([e for e in lst if type(e)!=int]))),
                    [])

