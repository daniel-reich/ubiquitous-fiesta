
def check_pattern(lst, pat):
  c1 = all([len({tuple(lst[i]) for i in range(len(lst)) if pat[i]==l})==1 for l in set(pat)])
  c2 = len({tuple({tuple(lst[i]) for i in range(len(lst)) if pat[i]==l}) for l in set(pat)})==len(set(pat))
  return c1 and c2

