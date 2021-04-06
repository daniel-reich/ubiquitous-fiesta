
def number_len_sort(lst):
    return sorted(lst, key=lox)
​
def lox(x):
    return len(str(x))

