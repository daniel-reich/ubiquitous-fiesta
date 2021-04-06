
def big_sub(lst):
    best_sum, current_sum = lst[0] , lst[0]
    start = [0]
    end = 0
    for i in range(1,len(lst)):
        if len(start) > 4:
            start = [0] 
        current_sum = max(lst[i],current_sum + lst[i])
        if current_sum >= best_sum:
            best_sum = current_sum
            end = i
        if current_sum <= 0:
            start.append(i + 1)
    return [best_sum,start[-1] if start[-1] <= end else start[-2],end]

