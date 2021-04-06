
def fauna_number(txt):
    #iterate through list <animals> and check if animal exists in list <txt>
    #if animal exists, store animal in list <exists>
    #sort list <exists> based on order of appearance in string <txt>
    #for each animal in exists
    #get starting index of animal in string
    #iterate through the string backwards from index - 2 until not digit
    #add 1 to start and end to adjust
    #store animal and number in tuple and append to list <result>
​
    animals = ["muggercrocodile","one-hornedrhino","python","moth","monitorlizard","bengaltiger"]
    result = []
    exists = []
    for animal in animals:
        if animal in txt:
            exists.append(animal)
    exists.sort(key=txt.index)
    for animal in exists:
        end = txt.index(animal) - 2
        start = end
        while txt[start].isdigit():
            start -= 1
        result.append((animal, txt[start + 1: end + 1]))
    return result

