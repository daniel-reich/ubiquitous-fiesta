
def largest_even(arr):
    answer = -1
    for num in arr:
        if num % 2 == 0 and num > answer:
            answer = num
    return answer

