
def numbers_need_friends_too(n):
  new_num = ''
  n_str = str(n)
  for i, v in enumerate(n_str):
    if i == 0 and n_str[i+1] != v:
      new_num += v * 3
    elif i == len(n_str) - 1 and n_str[i - 1] != v:
      new_num += v * 3
    elif n_str[i-1] != v and n_str[i+1] != v:
      new_num += v * 3
    else:
      new_num += v
  return int(new_num)

