
import re  
    
def convert_x_element(element):
​
    if re.search("^-", element):
        sign = - 1
    else:
        sign = 1
   
    return sign * int(''.join(re.findall("\d", element)))
​
​
def convert_y_element(element, sign):
    
    return sign * int(element)
​
def will_hit(trajectory, position):
    
    sign = 1
    trajectory_list = trajectory.split()
​
    for element in trajectory_list:
        if re.search("x$", element):  
            x_number = convert_x_element(element)
        elif element == '-':
            sign = -1
        elif re.search("\d", element):
            y_number = convert_y_element(element, sign)
​
    if position[1] == x_number * position[0] + y_number:
        return True
    
    return False

