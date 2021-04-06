
def join(text_list):
    result_text = ""
    overlapping_min = 0
    overlappings = []
    length = len(text_list)
    if length <=1:
        return [result_text, overlapping_min]
    
    result_text = text_list[0]
    for i in range(1,length):
        prev_text = text_list[i-1]
        current_text = text_list[i]
        current_len = len(text_list[i])
        count = 0
        start_letter = current_text[0]
        for j in range(len(prev_text)):
            count = 0
            if prev_text[j] == start_letter:
                suffix_len = len(prev_text[j:])
                if suffix_len <= current_len:
                    if prev_text[j:] == current_text[:suffix_len]:
                        count = suffix_len
                        
                        break
        overlappings.append(count)
        result_text += current_text[count:]
    overlapping_min = min(overlappings)
    return [result_text,overlapping_min]

