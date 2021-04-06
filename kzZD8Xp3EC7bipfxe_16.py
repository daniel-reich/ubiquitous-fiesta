
def worded_math(equ):
    nums = ['zero', 'one', 'two']
    lst = equ.split()
    if lst[1].lower() == 'plus':
        return nums[nums.index(lst[0].lower())
                    + nums.index(lst[2].lower())].capitalize()
    elif lst[1].lower() == 'minus':
        return nums[nums.index(lst[0].lower())
                    - nums.index(lst[2].lower())].capitalize()

