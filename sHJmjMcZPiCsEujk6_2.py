
def pilish_string(txt):
    result = ""
    done = False
    nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    counter = 0
    prevCounter = 0
    index = 0
    while not done:
        counter = counter + nums[index]
        if (txt[prevCounter:counter] == ""):
            done = True
            break
​
        if (len(txt[prevCounter:counter]) == nums[index]):
            result = result +  " " + txt[prevCounter:counter]
        elif(len(txt[prevCounter:counter]) < nums[index]):
            x = nums[index] - len(txt[prevCounter:counter])
            lastLetter = txt[prevCounter:counter][-1]
            word = ""
            for i in range(x):
                word = word + lastLetter
            result = result + " " + txt[prevCounter:counter] + word
        prevCounter = counter
        if ((index == len(nums)-1) ):
            done = True
        index = index+1
    return result[1:]
​
​
​
# Test.assert_equals(pilish_string("FORALOOP"), "FOR A LOOP")
​
#print(pilish_string('CANIMAKEAGUESSNOW'))

