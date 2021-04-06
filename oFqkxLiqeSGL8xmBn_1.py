
def add_two_numbers(l1, l2):
    res = ListNode()
    cur_res = res
    rem = 0
    while l1 or l2:
        add_val = rem
        if l1 and l2:
            add_val += l1.val + l2.val
            l1 = l1.next
            l2 = l2.next
        elif l1:
            add_val += l1.val
            l1 = l1.next
        elif l2:
            add_val += l2.val
            l2 = l2.next
        if add_val > 9:
            rem, add_val = divmod(add_val, 10)
        else:
            rem = 0
        cur_res.val = add_val
        if l1 or l2:
            cur_res.next = ListNode()
            cur_res = cur_res.next
        elif rem:
            cur_res.next = ListNode(rem)
    return res

