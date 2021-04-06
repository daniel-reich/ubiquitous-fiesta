
def clean_up_list(lst):
    even, odd = [], []
    for i in lst:
        odd.append(int(i)) if int(i)%2 else even.append(int(i))
    return [even, odd]

