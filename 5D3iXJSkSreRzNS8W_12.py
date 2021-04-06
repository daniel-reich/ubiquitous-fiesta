
def news_at_ten(txt, n):
  output = [" "*n] 
  txt_not_on_screen = list(txt) + [" "]*n
  last_item = " "*n
  while last_item != " "*n or len(output) == 1:
    last_item = last_item[1:] + txt_not_on_screen[0]
    output.append(last_item)
    txt_not_on_screen.pop(0)
  return output

