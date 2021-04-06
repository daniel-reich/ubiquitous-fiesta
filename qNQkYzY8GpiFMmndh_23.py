
def join(lst: list):
    result, shared_letters = lst[0], []
    paired_list = list(zip(lst, lst[1:]))
    for pair in paired_list:
        word1, word2 = pair[0], pair[1]
        last_letter = word1[-1]
        for i, letter in enumerate(word2):
            if letter not in word1:  # add letter if it is not found in word1
                result += letter
            elif letter in word1 and letter == last_letter:  # add the remainder slice of the word
                result += word2[i + 1:]
                shared_letters.append(i + 1)
                break
    return [result, min(shared_letters) if shared_letters else 0]

