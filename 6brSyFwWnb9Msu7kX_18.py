
def pos_neg_sort(lst):
    positives = sorted(filter(lambda x: x > 0, lst), reverse= True)
    indexes = list(map(lambda x: x > 0 , lst))
    return [lst[i] if indexes[i]==False else positives.pop() for i in range(len(indexes))]

