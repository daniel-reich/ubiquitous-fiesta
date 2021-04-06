
def available_spots(lst, num):
    evenodd = [i%2 for i in lst]
    n = num%2
    return sum(n in [x,y] for x,y in zip(evenodd, evenodd[1:]))

