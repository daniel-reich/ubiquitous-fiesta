
import itertools
​
def factors(n):
    f = 2
    increments = itertools.chain([1,2,2], itertools.cycle([4,2,4,2,4,6,2,6]))
    for incr in increments:
        if f*f > n:
            break
        while n % f == 0:
            yield f
            n //= f
        f += incr
    if n > 1:
        yield n
​
seq = [1, 2]
queue = list(range(3, 1000))
last_factors = set(factors(seq[-1]))
while len(queue) > 0:
    idx = 0
    while True:
        cur = queue[idx]
        cur_factors = set(factors(cur))
        if len(last_factors.intersection(cur_factors)) > 0:
            # number found
            break
        idx += 1
        if idx >= len(queue):
            break
    if idx >= len(queue):
        break
    queue.pop(idx)
    seq.append(cur)
    last_factors = cur_factors  
​
def ecg_seq_index(n):
    return seq.index(n)

