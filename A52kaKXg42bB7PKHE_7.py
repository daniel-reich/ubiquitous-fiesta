
def num_then_char(sample):
        
    def sortBoth(lst):
        letters = []
        nums = []
        for i in lst:
            if type(i) == int or type(i) == float:
                nums.append(i)
            else:
                letters.append(i)
        output = []
        letters = sorted(letters)
        nums = sorted(nums)
        for num in nums:
            output.append(num)
        for letter in letters:
            output.append(letter)
        return output
    lstCount = 0
    lengths = []
    for lst in sample:
        lstCount += 1
        lengths.append(len(lst))
​
   # print(lstCount, lengths)
​
    # def lstGetter(lst, subsets):
    #     output = []
    #     start = 0
    #     before = 0
    #     for s in subsets:
​
    full = []
    for lst in sample:
        for e in lst:
            full.append(e)
​
    full = sortBoth(full)
    output = []
    for l in lengths:
        lst = []
        for i in range(l):
        # print(i)
            lst.append(full[i])
        output.append(sortBoth(lst))
        #print(output)
        full = full[i + 1:]
    return output

