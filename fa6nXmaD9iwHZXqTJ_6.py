
def tf_lst(lst):
  a=lst[1]==round((lst[0]-10)*20)
  b=lst[4]==lst[1]//2
  c=(lst[2]==lst[4]//10 or lst[2]==lst[4]//10+1 or lst[2]==lst[4]//10+2 or lst[2]==lst[4]//10+3)
  d=lst[3]==lst[4]*321
  e=lst[5]==lst[2]+lst[4]
  f=lst[6]==lst[4]**2
  g=lst[7]==lst[4]+lst[1]/10
  return all([a,b,c,d,e,f,g])

