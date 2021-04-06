
def num_of_digits(num):
    count = 0
    absolut = abs(num)
    while absolut > 0:
        absolut = absolut//10
        count += 1
    if count == 0:
        return count + 1
    else:
        return count
​
print(num_of_digits(123))

