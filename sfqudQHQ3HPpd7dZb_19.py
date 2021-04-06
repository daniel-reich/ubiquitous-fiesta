
rps = lambda x, y: "It's a draw" if x == y else "The winner is p1" \
  if ({'R': 'Scissors', 'S': 'Paper', 'P': 'Rock'})[x[0]] == y else "The winner is p2"

