
def shuffle_count(num):
    shuffle = lambda lst: sum([[x,y] for x,y in zip(lst[:n//2],lst[n//2:])],[])
    order = list(range(1,n+1))
    cards, i = shuffle(order), 1
    while cards != order:
        cards = shuffle(cards)
        i +=1
    return i

