
def shuffle_count(num):
    deck = [i for i in range(1,num+ 1)]
    ans = [i for j in zip(deck[:len(deck)//2],deck[len(deck)//2:]) for i in j]
    counter = 1
    while ans != deck:
        ans = [i for j in zip(ans[:len(ans)//2],ans[len(ans)//2:]) for i in j]
        counter += 1
    return counter

