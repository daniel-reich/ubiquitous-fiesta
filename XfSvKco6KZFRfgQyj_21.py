
def find_a_seat(n, lst):
  shadow_lst, length = lst, 0
  while shadow_lst:
    length += 1
    shadow_lst = shadow_lst[1:]
  max_cap, count, empty = n/length, 0, []
  while lst:
    if lst[0] <= max_cap/2:
      empty += [count]
    count += 1
    lst = lst[1:]
  return empty[0] if empty else -1

