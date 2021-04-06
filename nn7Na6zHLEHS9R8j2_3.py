
def deep_count(alist):
    count = 0
    for element in alist:
        if not isinstance(element,list):
            count = count+1
        elif isinstance(element,list):
            count = count+1
            count = count + deep_count(element)
    return count

