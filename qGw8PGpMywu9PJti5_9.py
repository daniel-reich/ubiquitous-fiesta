
def hanoi(n):
    origin = 1
    aux = 2
    dest = 3
    history = []
    return towers_of_hanoi(n, origin, dest, aux, history)
​
def towers_of_hanoi(n, origin, dest, aux, history):
    if n <= 0:
        return history
    towers_of_hanoi(n-1, origin, aux, dest, history)
    history.append((origin, dest))
    return towers_of_hanoi(n-1, aux, dest, origin, history)

