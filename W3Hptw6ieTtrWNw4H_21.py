
def bifid(text):
    enc_flag = False
    for ele in text:
        if not ele.isalpha():
            enc_flag = True
            break
    coding_list = [chr(i) for i in range(ord('a'),ord('z')+1) if i != ord('j')]
    coding_table = {e:(i//5, i%5) for i,e in enumerate(coding_list)}
    coding_table_inverse = {coding_table[i]:i for i in coding_table}
    if enc_flag:
        new_text = ''.join([i.lower() for i in text if i.isalpha()])
        result_code_list = []
        for e in new_text:
            e = e.lower()
            if e == 'j':
                e = 'i'
            result_code_list.append(coding_table[e])
        temp_list = [e[i] for i in range(2) for e in result_code_list]
        result = ''.join([coding_table_inverse[(temp_list[i], temp_list[i+1])] for i in range(0, len(temp_list), 2)])
    else:
        result_code_list = []
        for e in text:
            code = coding_table[e]
            result_code_list.append(code[0])
            result_code_list.append(code[1])
        temp_list = []
        length = len(result_code_list)
        for i in range(length//2):
            temp_list.append(result_code_list[i])
            temp_list.append(result_code_list[i+length//2])
        result = ''.join([coding_table_inverse[(temp_list[i], temp_list[i+1])] for i in range(0, len(temp_list), 2)])
            
    return result

