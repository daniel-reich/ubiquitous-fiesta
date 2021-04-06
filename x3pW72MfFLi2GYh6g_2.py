
def is_scalable(lst):
    return all(abs(lst[i] - lst[i - 1]) < 6 for i in range(1, len(lst)))

