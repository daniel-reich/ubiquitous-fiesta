
def shuffle_count(num):
    step = num // 2
    deck = [i for i in range(1,num+1)]
    lst = list(sum([(i,j) for i,j in zip(deck[:step],deck[step:])],()))
    counter = 1
    while lst != deck:
        lst = [(i,j) for i,j in zip(lst[:step],lst[step:])]
        lst = list(sum(lst,()))
        counter += 1
    return counter

