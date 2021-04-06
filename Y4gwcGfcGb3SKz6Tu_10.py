
def max_separator(txt):
  txt_dict = {}
  for i, v in enumerate(txt):
    if v in txt_dict:
      txt_dict[v].append(i)
    else:
      txt_dict[v] = [i]
  diff_dict = {}
  for k, v in txt_dict.items():
    if len(v) > 1:
      diff_dict[k] = max([v[i+1] - v[i] for i, x in enumerate(v) if i != len(v) - 1])
  if diff_dict:
    max_v = max(diff_dict.values())
    return sorted([k for k, v in diff_dict.items() if v == max_v])
  else:
    return []

