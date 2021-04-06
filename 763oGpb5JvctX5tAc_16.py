
#edabit
#check anagrams
​
def is_anagram(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()
    result = True
    if len(text1) != len(text2):
        result = False
    else:
        for t in text1:
            if t not in text2:
                result = False
                break
    return result
​
def main():
    pass
​
if __name__ == "__main__":
    main()

