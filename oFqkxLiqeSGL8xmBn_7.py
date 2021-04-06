
def add_two_numbers(l1, l2):
  num1 = int(''.join(list(map(str,l1.get_data()))[::-1]))
  num2 = int(''.join(list(map(str,l2.get_data()))[::-1]))
  addition = str(num1 + num2)[::-1]
  lst = [int(num) for num in str(addition)]
  l3 = ListNode(lst[0])
  l3.add_data(lst[1:])
  
  
  
  return l3

