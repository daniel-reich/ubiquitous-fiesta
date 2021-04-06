
def alternate_sort(lst):
    numbers, letters = [], []
    for i in lst:
        if type(i) == int:
            numbers.append(int(i))
        else:
            letters.append(i)
    result = list(zip(sorted(numbers), sorted(letters)))
    return [x for sub in result for x in sub]

