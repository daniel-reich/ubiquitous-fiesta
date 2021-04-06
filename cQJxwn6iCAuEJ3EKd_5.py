
def digits_count(num, count = 0):
    if abs(num) <10:
        return count + 1
    count+=1
    return digits_count(num/10,count)

