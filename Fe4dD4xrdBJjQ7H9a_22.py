
def who_wins_tonight(coins, space, price, size):
  return (
    'Bill' if coins//price > space//size else
    'Will' if coins//price < space//size else
    'Tie'
    )

