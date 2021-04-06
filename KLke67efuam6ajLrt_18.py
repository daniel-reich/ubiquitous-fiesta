
def shuffle(cards_list):
  num_cards = len(cards_list)
  return_list = []
  for i in range(num_cards//2):
    return_list.append(cards_list[i])
    return_list.append(cards_list[i+num_cards//2])
  return return_list
​
def shuffle_count(num):
  cards = list(i for i in range(1, num+1))
  new_shuffle = shuffle(cards)
  count = 1
  while cards != new_shuffle:
    new_shuffle = shuffle(new_shuffle)
    count += 1
  return count

