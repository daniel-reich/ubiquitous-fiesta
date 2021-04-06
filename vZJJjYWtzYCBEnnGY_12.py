
def briscola_score(my_deck1, my_deck2):
    d = {'A': 11, '3': 10, 'K': 4, 'Q': 3, 'J': 2,
         '2': 0, '4': 0, '5': 0, '6': 0, '7': 0}
    first = sum(d[x[0]] for x in my_deck1)
    second = sum(d[x[0]] for x in my_deck2)
    if first + second > 120:
        return 'You Win!'
    elif first + second < 120:
        return 'You Lose!'
    elif first + second == 120:
        return 'Draw!'

