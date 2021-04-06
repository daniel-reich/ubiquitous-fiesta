
def count_characters(lst):
    count = 0
    for i in lst:
        count = count + len(i)
    return count
​
print(count_characters(["234","wer"]))

