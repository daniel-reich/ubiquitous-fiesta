
def recaman(n):
    vals = []
    dups = []
    for i in range(n):
        val = first_reca(i, vals)
        if val < 0 or val in vals:
            val = second_reca(i, vals)
        vals.append(val)
    dups = find_dups(vals)
    output = "---> Recaman's sequence: " + str(vals) +    \
            "\n---> Duplicates for n = " + str(n) + ": " + str(dups)
    return output
    
def first_reca(n, nums):
    if n == 0:
        return 0
    return nums[n-1] - n
​
def second_reca(n, nums):
    if n == 0:
        return 0
    return nums[n-1] + n
​
# need to order duplicates in the order the 2nd value appears in the list.
def find_dups(lst):
    dups = {}
    d_list = []
    if lst == []:
        return []
    for num in lst:
        if lst.count(num) > 1:
            if num not in dups:
                i = lst.index(num)
                indx = lst.index(num, i+1) # index of duplicate
                dups[indx] = num
    for x in sorted(dups):     # sort by index (order of appearance)
        d_list.append(dups[x])
    return d_list

