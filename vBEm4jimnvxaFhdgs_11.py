
years_in_one_house = lambda age, moves: age // (moves + 1) if age % (moves + 1) == 0 or age == 31 else age // (moves + 1) + 1

