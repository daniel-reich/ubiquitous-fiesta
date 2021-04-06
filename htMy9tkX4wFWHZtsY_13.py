
def palindrome_time(lst):
    start_time = lst[:3]
    end_time = lst[3:]
    mins = [0, 11, 22, 33, 44, 55]
    hours = ['00', '01', '02', '03', '04', '05', '10', '11', 
             '12', '13', '14', '15', '20', '21', '22', '23']
​
    total = 0
    for h in hours:
        for m in mins:
            t = [int(h), m, int(h[::-1])]
            if start_time <= t <= end_time:
                total += 1
    return total

