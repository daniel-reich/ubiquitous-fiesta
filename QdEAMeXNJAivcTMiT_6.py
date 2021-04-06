
def boxes(weights):
    temp_sum = 0
    req_boxes = 0
    for n in weights:
        if  temp_sum + n <= 10:
            temp_sum += n
        else:
            req_boxes += 1
            temp_sum = n
    if temp_sum <= 10:
        req_boxes += 1
    return req_boxes

