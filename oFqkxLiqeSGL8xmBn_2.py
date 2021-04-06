
def add_two_numbers(l1, l2):
  ll = ListNode(0)
  res = ll
  carry = 0
  while l1 or l2 or carry:
    if l1:
      val_1 = l1.val
      l1 = l1.next
    else:
      val_1 = 0
    if l2:
      val_2 = l2.val
      l2 = l2.next
    else:
      val_2 = 0
    
    quot, rem = divmod(val_1 + val_2 + carry, 10)
    carry = quot
    ll.next = ListNode(rem)
    ll = ll.next
  return res.next

