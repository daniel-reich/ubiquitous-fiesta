
def markdown(symb):
  
  def inner(big_txt, small_txt):
    symbol = symb
    index = big_txt.lower().find(small_txt.lower())
    while index >= 0:
      space = big_txt.find(" ", index)
      if space == -1:
        space = len(big_txt)
      big_txt = big_txt[:index] + symbol + big_txt[index:space] + symbol + big_txt[space:]  
      print(big_txt)
      index = big_txt.lower().find(small_txt.lower(), index + len(symbol) + 1)
      print(index)
      
    return big_txt
  
  return inner

