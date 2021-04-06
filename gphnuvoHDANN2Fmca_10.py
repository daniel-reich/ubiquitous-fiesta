
def odd_sort(lst):
    odds = iter(sorted(n for n in lst if n % 2))
    return [next(odds) if n % 2 else n for n in lst]

