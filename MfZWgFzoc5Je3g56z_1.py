
import numpy as np
​
def translate(ran, num):
    np_sign = lambda x: "+" if np.sign(x)==1 or np.sign(x)==0 else '-'
​
    if num > ran**2:
        return str(num) + " is not in the range [0:" + str(ran**2) + "]"
    else:
        secret_number = ran**2-num
        num_one = secret_number - num
        if np.sign(num_one)==-1:
            num_two = num_one + (ran ** 2 + 1)
        else:
            num_two = num_one - (ran ** 2 + 1)
        if abs(num_one) < abs(num_two):
            return np_sign(num_one) + str(abs(num_one)) + " ---> " + str(secret_number)
        elif abs(num_one) > abs(num_two):
            return np_sign(num_two) + str(abs(num_two)) + " ---> " + str(secret_number)
        else:
            if np.sign(num_one)==-1:
                return np_sign(num_two) + str(abs(num_two)) + " or " + np_sign(num_one) + str(abs(num_one)) + " ---> " + str(secret_number)
            else:
                return np_sign(num_one) + str(abs(num_one)) + " or " + np_sign(num_two) + str(abs(num_two)) + " ---> " + str(secret_number)

