
def unique_sort(lst):
    unique = []
    for num in lst:
        if num not in unique:
            unique.append(num)
​
    return sorted(unique)

