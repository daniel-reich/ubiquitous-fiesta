
def find_all_digits(nums):
​
    nums_gathered = []
    have_all_nums = False
​
​
    for i in nums:
        num_list = [int(x) for x in str(i)]
        v = num_list[0]
        w = num_list[1]
        y = num_list[2]
        z = num_list[3]
        
        if v not in nums_gathered:
            nums_gathered.append(v)
        if w not in nums_gathered:
            nums_gathered.append(w)
        if y not in nums_gathered:
            nums_gathered.append(y)
        if z not in nums_gathered:
            nums_gathered.append(z)
        
        if len(nums_gathered) == 10:
            return i
​
    return "Missing digits!"

