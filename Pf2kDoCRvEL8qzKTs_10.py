
def order_people(lst, people):
  if people > lst[0]*lst[1]:
    return 'overcrowded'
    
  nums = [0] * lst[0]*lst[1] + list(range(people, 0, -1))
  
  line = [[nums.pop() for i in range(lst[1])] for j in range(lst[0])]
  line = [i[::-1] if idx % 2 else i for idx, i in enumerate(line)]
  
  return line

