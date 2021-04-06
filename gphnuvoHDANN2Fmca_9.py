
def odd_sort(lst):
    odd_nums = [x for x in lst if x%2 != 0]
    odd_nums.sort()
​
    for num in range(len(lst)):
      if lst[num] % 2 != 0:
        del lst[num]
        lst.insert(num, odd_nums.pop(0))
    return lst

