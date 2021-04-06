
def check_flush(table, hand):
  suits = []
  temp = []
  count = [0,0,0,0] #[c,h,d,s]
  jam = table+hand
  for i in jam:
    temp += i.split('_')
  for i in temp:
    if i == 'C':
      count[0]+=1
    elif i == 'H':
      count[1]+=1
    elif i == 'D':
      count[2]+=1
    elif i == 'S':
      count[3]+=1
  return 5 in count or 6 in count or 7 in count

