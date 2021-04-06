
def bifid(text):
    grid = [['a', 'b', 'c', 'd', 'e'],
            ['f', 'g', 'h', 'i', 'k'],
            ['l', 'm', 'n', 'o', 'p'],
            ['q', 'r', 's', 't', 'u'],
            ['v', 'w', 'x', 'y', 'z']]
    rev = {char: (row_idx+1, col_idx+1) for row_idx,row in enumerate(grid) for col_idx, char in enumerate(row)}
    rev.update({'j': rev['i']})
    def unpolybius(nums):
        return ''.join([grid[int(a)-1][int(b)-1] for a,b in zip(nums[::2],nums[1::2])])
    def polybius(text):
        return [num for char in text if char in rev for num in rev[char]]
    nums = polybius(text.lower())
    nums = nums[::2] + nums[1::2] if ' ' in text else [num for pair in zip(nums, nums[len(nums)//2:]) for num in pair]
    return unpolybius(nums)

