
def tri_insertion(list):
    for j in range(1, len(list)):
        cle = list[j]
        i = j - 1
        while i >= 0 and list[i] > cle:
            list[i + 1] = list[i]
            i = i - 1
        list[i + 1] = cle
​
def duplicate_nums(nums):
    _size = len(nums) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if nums[i] == nums[j] and nums[i] not in repeated: 
                repeated.append(nums[i]) 
    if not repeated == []:
        tri_insertion(repeated)
        return repeated

