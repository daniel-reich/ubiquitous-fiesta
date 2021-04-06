
import re
def count_ones(lst):
    my_str = ""
    for i in range (0,len(lst)):
        my_str+=str(lst[i])
    #print(my_str)
    x = re.split('0',my_str)
    #print(x)
    count = 0
    string = ""
    for i in range (0,len(x)):
        string = x[i]
        if (len(string)>1):
            count+=1
    return count
​
print(count_ones([1, 0, 1, 0, 1, 0, 1, 0]))

