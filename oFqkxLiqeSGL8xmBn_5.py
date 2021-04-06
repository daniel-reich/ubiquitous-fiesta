
def add_two_numbers(l1, l2):
    s = [int(_) for _ in str(int(''.join(map(str, l1.get_data()[::-1]))) + int(''.join(map(str, l2.get_data()[::-1]))))][::-1]
    root = ListNode(s[0])
    root.add_data(s[1:])
    return root

