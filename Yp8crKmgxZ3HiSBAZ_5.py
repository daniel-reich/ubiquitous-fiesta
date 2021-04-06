
def freq_count(lst, el):
  def inner(lvl, freq, lst, el):
    if lvl not in freq:
      freq[lvl] = 0
    for ele in lst:
      if ele == el:
        freq[lvl] += 1
      elif isinstance(ele, list):
        inner(lvl + 1, freq, ele, el)
      else:
        pass
  freqs = {}
  inner(0, freqs, lst, el)
  return [[lvl, freq] for lvl, freq in freqs.items()]

