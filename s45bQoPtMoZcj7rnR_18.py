
from itertools import count
​
def closest_palindrome(num):
    if str(num) == str(num)[::-1]:
        return num
    for i in count(1):
        if str(num-i) == str(num-i)[::-1]:
            return num-i
        if str(num+i) == str(num+i)[::-1]:
            return num+i

