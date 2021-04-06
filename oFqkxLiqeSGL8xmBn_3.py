
def add_two_numbers(l1, l2):
  head, cur, carry = None, None, 0
  while l1 or l2:
    v = ((l1.val if l1 else 0) + (l2.val if l2 else 0) + carry)
    carry = v // 10
    new_node = ListNode(v % 10)
    if not head:
      head = cur = new_node
    else:
      cur.next = new_node
      cur = new_node
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None
  if carry:
    cur.next = ListNode(carry)
  return head

