
from collections import Counter
def hidden_anagram(text, phrase):
    phrase = phrase.replace(' ', '')
    phrase = phrase.lower()
    text_1 = ''
    for char in text:
        if char.isalpha():
            text_1 += char.lower()
    if phrase == '':
        return ""
    if len(phrase) == 1 and phrase[0] in text:
        return phrase[0]
    elif len(phrase) == 1 and phrase[0] not in text:
        return "noutfond"
    left = 0
    right = 0
    cnt_phrase = Counter(phrase)
    while right < len(text_1):
        if text_1[right] in phrase and right - left < len(phrase) -1:
            right += 1
        elif text_1[right] in phrase and right - left == len(phrase)-1 and right < len(text_1) -1:
            cnt_result = Counter(text_1[left:right+1])
            if all(cnt_phrase[key] == cnt_result[key] for key in cnt_phrase):
                return text_1[left:right+1]
            else:
                left += 1
                right += 1
        elif text_1[right] not in phrase and right < len(text_1) - 1:
            left += 1
            right += 1
        elif text_1[right] in phrase and right - left == len(phrase)-1 and right == len(text_1) -1:
            cnt_result = Counter(text_1[left:right + 1])
            if all(cnt_phrase[key] == cnt_result[key] for key in cnt_phrase):
                return text_1[left:right + 1]
            else:
                break
        elif text_1[right] not in phrase  and right == len(text_1) - 1:
            break
    return "noutfond"

