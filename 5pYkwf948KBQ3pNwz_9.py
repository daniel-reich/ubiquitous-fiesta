
import collections
import unicodedata
import itertools
​
​
def _segment_into_words(text):
    return [
        ''.join(elements).lower()
        for category, elements in itertools.groupby(
            text,
            key=lambda character: unicodedata.category(character)[0]
        )
        if category == 'L'
    ]
    
​
def most_common_words(text, n):
    words = _segment_into_words(text)
    counts = collections.Counter(words)
​
    try:
        count_threshold = sorted(counts.values(), reverse=True)[n]
    except IndexError:
        count_threshold = 0
​
    word_preference = sorted(
        counts.keys(),
        key=lambda word: (-counts[word], words.index(word)),
    )
​
    return {
        word: counts[word]
        for word in word_preference[:n]
    }

