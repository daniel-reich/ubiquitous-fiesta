
def turn_calc(num):
  dic = {'1':'I', '2':'Z', '3':'E', '4':'H', '5':'S', '6':'G', '7':'L', '8':'B', '9':'', '0':'O', '.':''}
  return ''.join([dic[i] for i in str(num)[::-1]])

