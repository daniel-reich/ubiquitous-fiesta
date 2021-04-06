
def final_result(lst):
    result = lst
    start, end = 0, 0
    while start < len(result) - 1:
        end = start
        while end < len(result) and result[end] == result[start]:
            end += 1
        if end > start + 1:
            left = result[:start] if start > 0 else [] 
            right = result[end:] if end < len(result) else []
            result = left + right
            start = 0
        else:
            start += 1
    return result

