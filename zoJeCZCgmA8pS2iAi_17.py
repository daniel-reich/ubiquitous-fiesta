
def func_sort(lst):
   b=[]
   for i in lst:
      k=0
      while callable(i):
         a=i()
         i=a
         k+=1
      b.append(k)
   zipped_lists = zip(b, lst)
   sorted_pairs = sorted(zipped_lists)
   tuples = zip(*sorted_pairs)
   list1, list2 = [list(tuple) for tuple in tuples]
   return (list2)

