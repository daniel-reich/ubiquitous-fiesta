
def add_two_numbers(l1, l2):
  a = int("".join(map(str,l1.get_data()[::-1])))
  b = int("".join(map(str,l2.get_data()[::-1])))
  num_list = list(map(int,list(str(a + b))))[::-1]
  answer = ListNode(num_list[0])
  answer.add_data(num_list[1:])
  return answer

