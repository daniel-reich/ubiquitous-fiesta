
def freq_count(lst, el):
  level_counts = [[0, 0]]
  for element in lst:
    if element == el:
      level_counts[0][1] += 1
    elif type(element) == list:
      sub_level_counts = freq_count(element, el)
      for i in range(len(sub_level_counts)):
        if len(level_counts) < i+2:
          level_counts.append([i+1, 0])
        level_counts[i+1][1] += sub_level_counts[i][1]
  return level_counts

