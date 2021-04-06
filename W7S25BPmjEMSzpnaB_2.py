
def n_bonacci_generator(n, k):
    if k == 1:
        yield 0
        return
    if n == 1:
        for _ in range(k):
            yield 1
    base = [0 for _ in range(n - 1)]
    for _ in range(n - 1):
        yield 0
    yield 1
    base.append(0)
    base.append(1)
    for _ in range(k - n):
        for i in range(n):
            base[i] = base[i + 1]
        base[n] = 0
        base[n] = sum(base)
        yield base[n]
​
  
def bonacci(N, k):
  return list(n_bonacci_generator(N, k))[-1]

