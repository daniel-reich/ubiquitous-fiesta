
def add_two_numbers(l1, l2):
  car, val = divmod(l1.val+l2.val, 10)
  l1 = l1.next
  l2 = l2.next
  ans = ListNode(val)
  curr = ans
  
  while l1 or l2 or car:
    car, val = divmod((l1.val if l1 else 0) + 
                        (l2.val if l2 else 0) +
                        car, 10)
    curr.next = ListNode(val)
    curr = curr.next
    if l1:
      l1 = l1.next
    if l2:
      l2 = l2.next
  
  return ans

