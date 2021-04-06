
def advanced_sort(lst: list) -> list:
    return [[occurrence] * lst.count(occurrence) for occurrence in sorted(set(lst), key=lst.index)]

