
def longest_7segment_word(lst):
    prohibited = "kmvxw"
    arr = []
    for i in lst:
        for x in i:
            if x in prohibited:
                arr.append(i)
    answer = []
    for i in lst:
        if i not in arr:
            answer.append(i)
    answer = sorted(answer, key=len)
    answer2 = []
    for i in answer:
        if len(i) == len(answer[-1]):
            answer2.append(i)
​
    if len(answer) > 0:
        return answer2[0]
    return ""

