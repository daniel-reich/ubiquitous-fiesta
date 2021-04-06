
def next_in_line(lst, num):
    if not lst:
        return "No list has been selected"
    else:
        lst.append(num)
        del lst[0]
        return lst
​
print(next_in_line([3,4,5,6,7],8))

