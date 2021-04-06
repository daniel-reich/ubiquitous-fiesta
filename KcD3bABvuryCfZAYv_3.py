
def most_frequent_char(lst):
    data = {}
    for word in lst:
        for char in word:
            if char in data:
                data[char] += 1
            else:
                data[char] = 1
​
    print(data)
    count_list = data.values()
    print(count_list)
​
    max_freq = max(count_list)
    print(max_freq)
​
    answer = []
    for k,v in data.items():
        if v == max_freq:
            answer.append(k)
    answer.sort()
    return answer

