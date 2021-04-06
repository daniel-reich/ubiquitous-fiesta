
def maxmin(n):
    minie = str(n)
    maxie = str(n)
    num_list = list(str(n))
    length=len(num_list)
    
    for first in range (0,length-1):
        for second in range (first+1, length):
            if first == 0 and num_list [second] == "0":
                continue
            else:
                new_list = num_list.copy()
                new_list[first] = num_list [second]
                new_list[second] = num_list [first]
                new_string = "".join(new_list)
                if new_string < minie:
                    minie = new_string
                elif new_string > maxie:
                    maxie = new_string
                    
    return (int(maxie), int(minie))

