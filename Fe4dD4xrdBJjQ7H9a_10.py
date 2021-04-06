
who_wins_tonight = lambda coins, space, price, size: 'Bill' if coins//price>space//size else 'Will' if coins//price<space//size else 'Tie'

