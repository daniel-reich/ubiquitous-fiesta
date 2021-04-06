
def fib_fast(num : int):
    if num == 0:
        return 0
    if num == 1:
        return 1
​
    temp_prev = 1
    temp_prev_prev = 0
​
    iteration = 1
    while iteration != num:
        temp_prev, temp_prev_prev = temp_prev + temp_prev_prev, temp_prev
        iteration += 1
    return temp_prev

