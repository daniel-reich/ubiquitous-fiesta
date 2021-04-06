
def overlap(s1, s2):
    for i in range(len(s1)):
        first_text = s1[i:]
        if first_text in s2 and first_text == s2[0:len(first_text)]:
            return s1[0:i] + s2
​
    return s1 + s2

