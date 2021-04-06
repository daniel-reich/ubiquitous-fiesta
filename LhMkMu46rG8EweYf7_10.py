
def first_letter(str):
    for i in range(len(str)):
        if str[i].isalpha(): return str[i]
​
def sort_by_letter(lst):
    return sorted(lst, key=first_letter)

