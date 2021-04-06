
def card_hide(card):
  last_num = card[-4:]
  first_num = card[:-4]
  star =""
  for n in range(len(first_num)):
    star+="*"
​
  return star+last_num

