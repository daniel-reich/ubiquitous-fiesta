
def find_broken_keys(txt1, txt2):
    array = []
​
    l1 = list(txt1)
    l2 = list(txt2)
​
    for i in range(len(l1)):
        if l2[i] != l1[i]:
            array.append(l1[i])
​
    answer = []
    for i in array:
        if i not in answer:
            answer.append(i)
​
    return answer

