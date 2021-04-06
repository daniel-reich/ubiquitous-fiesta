
def kix_code(addr):
​
  address = addr.split(',')
​
  second_part = address[1].split()
  third_part = address[2].split()
​
  post_code = third_part[:2]
  
  startn = None
  for n in reversed(range(0, len(second_part))):
    item = second_part[n]
    try:
      i = int(item)
      startn = n
      break
    except ValueError:
      if '-' in item:
        item = item.split('-')
        try:
          i = int(item[0])
          startn = n
          break
        except ValueError:
​
          continue
      else:
        continue#
  if startn == None:
    house_num = second_part[-1]
  else:
    house_num = 'X'.join(second_part[startn:]).replace('-','X')
​
  pc = ''
​
  for item in post_code:
    pc += item 
​
  tr = pc + house_num
​
  return tr.upper().replace('/', 'X')

