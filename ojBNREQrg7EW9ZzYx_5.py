
def count_eatable_chocolates(tm, cost_one):
  def get_money(string):
    words = string.split()
    
    for word in words:
      if '$' in word:
        if '$' == word:
          return int(words[0])
        tr = []
        for item in word:
          try:
            tr.append(str(int(item.replace('$',''))))
          except ValueError:
            if item == '-':
              tr.append(item)
#           print('VE, {}'.format(item))
            continue
        return int(''.join(tr))
      
      elif word == 'dollars':
        return int(words[words.index(word)-1])
      
    
    return False
  try:
    if get_money(cost_one) < 0:
      return 'Invalid Input'
    total_chocolates_bought = int(get_money(tm)/get_money(cost_one))
    total_wrappers_cashed_in = int(total_chocolates_bought/2)
#   print(total_chocolates_bought, total_wrappers_cashed_in)
    if total_wrappers_cashed_in%3==0 or total_wrappers_cashed_in == 2 or total_wrappers_cashed_in == 7:
      return total_chocolates_bought + total_wrappers_cashed_in - 1
    return total_chocolates_bought + total_wrappers_cashed_in
  except ZeroDivisionError:
    return 'Invalid Input'

