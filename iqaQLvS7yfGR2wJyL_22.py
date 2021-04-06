
def num_of_digits(num):
    count=0
    for i in str(num):
        if i.isdigit():
            count+=1
    return count

