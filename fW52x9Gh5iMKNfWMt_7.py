
def recaman_index(n):
    size, last = 2, 1
    found = {1}
​
    while last != n:
        new = last - size
        if new > 0 and new not in found:
            found.add(new)
            last = new
        else:
            last += size
            found.add(last)
        size += 1
​
    return size - 1

