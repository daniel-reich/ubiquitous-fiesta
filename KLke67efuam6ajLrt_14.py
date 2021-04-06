
def shuffle_count(num):
    lst_num = [i for i in range(1, num+1)]
    lst_num_copy = [i for i in range(1, num+1)]
    cnt = 0
    num_1 = [1] * num
    while True:
        for i in range(num// 2):
            num_1[2 * i] = lst_num[i]
            num_1[2 * i + 1] = lst_num[num//2 + i]
        cnt += 1
        lst_num = num_1.copy()
        if all(num_1[i] == lst_num_copy[i] for i in range(0, num)):
            return cnt

