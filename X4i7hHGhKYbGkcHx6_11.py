
def average_index(letters):
    return round(sum(list(map(lambda x:ord(x)-96, list(letters))))/len(letters),2)

