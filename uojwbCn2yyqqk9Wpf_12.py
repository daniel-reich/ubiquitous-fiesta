
def is_untouchable(number):
    lst = [i for i in range(2,number**2+1)]
    div = [[1] for x in lst]
    for i in range(len(lst)):
        for num in range(2,int(lst[i] ** 0.5)+1):
            if lst[i] % num == 0:
                div[i].append(num)
                if lst[i] // num not in div[i]:
                    div[i].append(lst[i] // num)
    ans = [lst[i] for i in range(len(lst)) if sum(div[i]) == number]
    return 'Invalid Input' if number <= 1 else ans if len(ans) > 0 else True

