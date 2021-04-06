
def text_to_number_binary(txt):
  lst = txt.split()
  num_lst = []
  for i in lst:
    if 'zero' == i.lower():
      num_lst.append('0')
    if 'one' == i.lower():
      num_lst.append('1')
  return ''.join(num_lst[:8 * (len(num_lst) // 8)])

