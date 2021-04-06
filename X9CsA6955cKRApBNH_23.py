
def longest_run(lst):
  a = ['1'] + list('1' if abs(lst[i]-lst[i-1])==1 and lst[i] != lst[i-2]   else '%1' for i in range(1,len(lst)))
  return len(lst) if "".join(a).count('%')==0 else max(len(j) for j in "".join(a).split('%'))

