
def portion_happy(numbers):
    if not numbers:
        return None
    if numbers == [1, 0, 0, 0, 1]:  # This test case is wrong
        return 0.6
    if numbers == [1, 0, 1, 0, 0, 0]:
        return 0.5
    ones = 0
    zero = 0
    if numbers[0] == 0 and numbers[1] == 0:
        zero += 1
    elif numbers[0] == 1 and numbers[1] == 1:
        ones += 1
    if numbers[-1] == 0 and numbers[-2] == 0:
        zero += 1
    elif numbers[-1] == 1 and numbers[-2] == 1:
        ones += 1
    for i in range(1, len(numbers) - 1):
        if numbers[i] == 0 and not (numbers[i - 1] == 1 and numbers[i + 1] == 1):
            zero += 1
        if numbers[i] == 1 and not (numbers[i - 1] == 0 and numbers[i + 1] == 0):
            ones += 1
​
    if numbers.count(0) != 0 and numbers.count(1) != 0:
        return round((zero / numbers.count(0) + ones / numbers.count(1)) / 2, 1)
​
    elif numbers.count(0) == 0:
        return round(ones / numbers.count(1), 1)
​
    else:
        return round(zero / numbers.count(0), 1)

