
def multiply_nums(nums):
    new_nums = ""
    total = 1
​
    for char in nums:
        if char == ",":
            continue
        new_nums += char
​
    edited = new_nums.split()
    
    for number in edited:
        total *= int(number)
​
    return total

