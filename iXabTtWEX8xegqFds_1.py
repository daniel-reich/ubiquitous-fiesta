
def alternate_sort(lst):
    numbers = sorted(filter(lambda x: isinstance(x, int), lst))
    letters = sorted(filter(lambda x: isinstance(x, str), lst))
    return [c for combo in zip(numbers, letters) for c in combo]

