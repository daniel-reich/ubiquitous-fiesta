
def word_construction(original):
    result_original = []
    left = 0
    right = 0
    cnt = 0
    while right < len(original):
        if right < len(original) - 1:
            if original[left] == original[right]:
                cnt += 1
                right += 1
            else:
                result_original.append([original[left], cnt])
                left = right
                cnt = 0
        elif right == len(original) - 1:
            if original[left] == original[right]:
                cnt += 1
                result_original.append([original[left], cnt])
                break
            else:
                result_original.append([original[left], cnt])
                result_original.append([original[right], 1])
                break
    return result_original
​
​
def is_long_pressed_word(original, typed):
    result_original = word_construction(original)
    result_typed = word_construction(typed)
    if len(result_original) != len(result_typed):
        return False
    for i in range(len(result_original)):
        if result_typed[i][1] < result_original[i][1]:
            return False
    return True
​
​
def is_long_pressed(original, typed):
    if " " not in original:
        return is_long_pressed_word(original, typed)
    else:
        original_split = original.split()
        typed_split = typed.split()
​
        if len(original_split) != len(typed_split):
            return False
        for i in range(len(original_split)):
            if not is_long_pressed_word(original_split[i], typed_split[i]):
                return False
    return True

