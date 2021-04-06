
def insertions_sort(lst):
    has = True
    while has:
        has = False
        for indexex in range(1,len(lst)):
            current_number = lst[indexex]
            last_numer = lst[indexex-1]
            if last_numer > current_number:
                has = True
                temp = last_numer
                lst[indexex-1] = current_number
                lst[indexex] = temp
    return lst
​
def revers(lst):
    order_parts = []
    for parts in lst:
        order_parts.insert(0, parts)
    return order_parts
​
​
def sort_dates(lst, mode):
    times = {}
    for dates in lst:
        parts = dates.split("_")
        x = parts[0].split("-") + parts[1].split(":")
        orderd_times = int(x[2]+x[1]+x[0]+x[3]+x[4])
        times[orderd_times] = dates
    orderd_time = insertions_sort(list(times.keys()))
    list_of_orderd_times = []
    for things in orderd_time:
        list_of_orderd_times.append(times[things])
​
    if mode == "DSC":
        return revers(list_of_orderd_times)
    else:
        return list_of_orderd_times

