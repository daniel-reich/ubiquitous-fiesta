
def move_disk(r_fr, r_to):
    res.append((r_fr, r_to))
​
def get_mid(r_fr, r_to):
    check = r_fr + r_to
    if check == 3:
        return 3
    elif check == 4:
        return 2
    else:
        return 1
​
def move_rod(r_fr, n, r_to):
    if n == 1:
        move_disk(r_fr, r_to)
    else:
        r_mid = get_mid(r_fr, r_to)
        move_rod(r_fr, n-1, r_mid)
        move_disk(r_fr, r_to)
        move_rod(r_mid, n-1, r_to)
​
def hanoi(n):
  global res
  res = []
  if n == 0:
    return res
  move_rod(1, n, 3)
  return res

