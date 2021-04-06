
def alpha_range(start, stop, step=1):
    output = []
​
    # check error ranges.
    if (step == 0) or (step <= -26) or (step >= 26):
        return "step must be a non-zero value between -26 and 26, exclusive"
​
    # ensure both are the same case.  
    both_upper = start.isupper() and stop.isupper()
    both_lower = start.islower() and stop.islower()
    if not(both_upper or both_lower):
        return "both start and stop must share the same case"
​
    # convert character ranges to their ASCII numeric values.
    # 'a' - 'z' => 97 - 122
    # 'A' - 'Z' => 65 - 90
    start_num = ord(start)
    stop_num = ord(stop)
​
    # forwards
    if step > 0:
        if start_num > stop_num:
            start_num, stop_num = stop_num, start_num
​
        for num in range (start_num, stop_num+1, step):
            output.append(chr(num))
            
    # backwards
    if step < 0:
        if start_num < stop_num:
            start_num, stop_num = stop_num, start_num
​
        for num in range(start_num, stop_num-1, step):
            output.append(chr(num))
​
    return output

