
def same_vowel_group(arr):
    vowels = ['a','e','i','o','u']
    vowelsInFirst = []
    countOfFirst = 0
    result = []
​
    for i in arr[0]:
        if (i in vowels) and (i not in vowelsInFirst):
            vowelsInFirst.append(i)
            countOfFirst += 1
    # print(vowelsInFirst,countOfFirst)
    for i in arr:
        temp = 0
        tempVowel = []
        for j in i:
            if (j in vowels) and (j not in tempVowel):
                tempVowel.append(j)
                temp += 1
        if (temp == countOfFirst) and (sorted(tempVowel) == sorted(vowelsInFirst)):
            # print("asdfgh",sorted(tempVowel), sorted(vowelsInFirst))
            result.append(i)
        # print("Temp",tempVowel,temp)
​
    return result

