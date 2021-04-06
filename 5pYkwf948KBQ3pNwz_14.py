
from collections import OrderedDict
​
def most_common_words(text, n):
    text_lst = text.split()
    result_lst = []
    for i in range(len(text_lst)):
        if text_lst[i].isalpha():
                result_lst.append(text_lst[i].lower())
        elif "'" in text_lst[i]:
             index = text_lst[i].find("'")
             result_lst.append(text_lst[i][:index].lower())
             result_lst.append(text_lst[i][index+1 :].lower())
        elif text_lst[i].endswith(".") or text_lst[i].endswith("?") or text_lst[i].endswith(",") or  text_lst[i].endswith("!"):
                 result_lst.append(text_lst[i][:-1])
    print(result_lst)
    result_dict = OrderedDict()
​
    for word in result_lst:
        if word not in result_dict:
            result_dict[word] = 1
        else:
            result_dict[word] += 1
    sort_list = sorted(result_dict.keys(), key = lambda x :result_dict[x], reverse = True)
    if n >= len(result_dict):
        return {word : result_dict[word] for word in sort_list}
    else:
        return {sort_list[i] : result_dict[sort_list[i]] for i in range(0, n)}

