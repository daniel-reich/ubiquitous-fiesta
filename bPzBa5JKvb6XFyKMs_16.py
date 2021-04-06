
primiera = { '7':21, '6':18, 'A':16, 'K':10, 'Q':10, \
              'J':10, '2': 12, '3':13, '4':14, '5':15 }
​
best_card = lambda cards,seme: max( primiera[c[0]] for c in cards if c[-1] == seme )
​
def get_primiera_score(cards):
  
  if sum(1 for s in 'dhsc' if s in ''.join(cards)) != 4:
    return 0
​
  else:
    return sum( map( lambda x: best_card(cards,x),'dhsc') )

