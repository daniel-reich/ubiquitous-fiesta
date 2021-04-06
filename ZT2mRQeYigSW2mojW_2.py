
vowels = "aeiouy"
​
def count_syllables2(word):
    word = ''.join([c for c in word if c.isalpha()])
    v_count = sum([c in vowels for c in word])
    if v_count == 1:
        return 1
    if word[-1] == "e" or word[-2:] == "es" or word[-3:] == "e's":
        v_count -= 1
    v_doubles = sum([word[i] in vowels and word[i-1] in vowels for i in range(1, len(word))])
    return max(1, v_count - v_doubles)
​
def count_syllables1(line):
    return sum([count_syllables2(word.lower().strip()) for word in line.split()]) 
​
def haiku(string):
    return [count_syllables1(line) for line in string.split('/')] == [5, 7, 5]

