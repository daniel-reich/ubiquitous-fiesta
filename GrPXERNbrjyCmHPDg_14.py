
def duplicate_count(txt):
  checked_list = []
  count = 0
  
  for each in txt:
    if each not in checked_list:
      if txt.count(each) > 1:
        count += 1
        checked_list.append(each)
        
  return count

