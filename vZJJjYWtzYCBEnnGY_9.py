
def briscola_score(my_deck1, my_deck2):
  a = {"A": 11, "3": 10,"K": 4,"Q": 3 ,"J": 2}
  b = sum(0if i[0] not in a else a[i[0]]for i in my_deck1)
  c = sum(0if i[0] not in a else a[i[0]]for i in my_deck2)
  return"You Win!"if b+c>120 else"You Lose!" if b+c<120 else "Draw!"

