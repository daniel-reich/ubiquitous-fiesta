
def reverse_sort(txt):
  lst=txt.split(' ')
  l1=sorted(sorted(lst,reverse=True),key=lambda x:x.lower(),reverse=True)
  l2=sorted(l1,key=len,reverse=True)
  s=''
  for i in l2:
    s=s+i+' '
  return s[:-1]

