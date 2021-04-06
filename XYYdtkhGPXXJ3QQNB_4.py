
def num_in_str(lst):
    w_nums = []
    for string in lst:
        for i in string:
            if i.isdigit():
                if string not in w_nums:
                    w_nums.append(string)
            
    return w_nums
                
​
        
        
num_in_str(['abc', 'ab12', 'dfaecd12', 'alskdgh'])

