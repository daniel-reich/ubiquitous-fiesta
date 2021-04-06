
from collections import deque
​
​
def palindrome_descendant(num):
    if check_palindrome(str(num)):
        return True
    else:
        num_desc_1 = add_digits(num)
        if len(str(num_desc_1)) >= 2:
            if check_palindrome(str(num_desc_1)):
                return True
            else:
                num_desc_2 = add_digits(num_desc_1)
                if len(str(num_desc_2)) >= 2:
                    return check_palindrome(str(num_desc_2))
                else:
                    return False
        else:
            return False
​
​
def check_palindrome(a_str):
    if len(a_str) % 2 == 0:
        if a_str[:int(len(a_str) / 2)] == a_str[-1:int(len(a_str) / 2 - 1):-1]:
            return True
        else:
            return False
    elif a_str[:int(len(a_str) / 2)] == a_str[-1:int(len(a_str) / 2):-1]:
            return True
    else:
        return False
​
​
def add_digits(num):
    num_str = deque(str(num))
    new_str = []
    while len(num_str) > 1:
        new_str.append(str(int(num_str.popleft()) + int(num_str.popleft())))
    if len(num_str) == 1:
        new_str.append(num_str.pop())
    return int("".join(new_str))

