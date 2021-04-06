
def digit_sort(lst):
    return sorted(sorted(lst), key=lambda n: len(str(n)), reverse=True)

