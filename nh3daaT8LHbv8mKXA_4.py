
def text_to_num(phone):
  alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',\
    'Q','R','S','T','U','V','W','X','Y','Z']
  num =[2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
  t = ''
  for i in range(len(phone)):
    if phone[i].isalpha():
      t = t + str(num[alpha.index(phone[i])])
    else:
      t = t + phone[i]
  return t

