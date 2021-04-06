
def sumOfDivisors(num):
    sumDivisors = 0
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            if num // i == i or num // i == num:
                sumDivisors += i
            else:
                sumDivisors += i + num // i
    return sumDivisors
​
​
def is_untouchable(number):
​
    if number < 2:
        return "Invalid Input"
​
    touchableList = []
    for i in range(2, number ** 2):
        if sumOfDivisors(i) == number:
            touchableList.append(i)
​
    if len(touchableList) > 0:
        return touchableList
    else:
        return True

