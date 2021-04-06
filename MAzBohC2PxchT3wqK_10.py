
def shadow_sentence(sentenceone,sentencetwo):
    sentenceone = sentenceone.split(' ')
    sentencetwo = sentencetwo.split(' ')
    for i in range(len(sentenceone)):
        try:
            if word_length(sentenceone[i]) != word_length(sentencetwo[i]):
                return False
            elif share_letters(sentenceone[i],sentencetwo[i]):
                return False
        except Exception as e:
            return False
    return True
​
​
def word_length(eachword):
    return len(eachword)
​
​
def share_letters(word1,word2):
    for eachletter in set(list(word1)):
        if eachletter in word2:
            return True
    return False

