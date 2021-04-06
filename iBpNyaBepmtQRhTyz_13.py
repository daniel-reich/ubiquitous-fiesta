
def c_cipher(msg, keyword):
​
    def decrpyt(msg, keyword):
        list1 = [letter for letter in msg]
        answer = [[] for i in range(0, int(len(msg)/len(keyword)))]
        print("Printing List1: ")
        print(list1)
        print("=" * 20)
​
        # appending items of list1 to list2 structure
        index = 0
        counter = 0
        for digit in list1:
            answer[index].append(digit)
            counter += 1
            if counter % len(keyword) == 0:
                index +=1
​
​
        #create dictionary for keyword
        keyword_list = [i for i in keyword]
        keyword_dict = {}
        keyword_dict = {i:keyword_list.index(i) for i in keyword}
        print(keyword_dict)
​
        # iterate through list2 and add the correct
        sorted_keyword_list = sorted([i for i in keyword])
        print(sorted_keyword_list)
​
​
        column_counter = 0
        row_counter = 0
        for i in list1:
            answer[row_counter][keyword_dict.get(sorted_keyword_list[column_counter])] = i
            row_counter +=1
            if row_counter == len(answer):
                row_counter = 0
                column_counter += 1
​
        final_answer = ""
        for list_item in answer:
            for char in list_item:
                final_answer += char
        print(answer)
        print(final_answer)
        return final_answer
​
​
​
​
​
​
​
​
​
​
​
    def encrypt(msg, keyword):
        import math
        list1 = [letter.lower() for letter in msg if letter.isalnum()]
        print("Printing List1: ")
        print(list1)
        print("=" * 20)
        if len(list1) % len(keyword) != 0:
            digits = int(len(list1) / len(keyword)) + 1
​
        else:
            digits = int(len(list1) / len(keyword))
​
        list2 = [[]for i in range(0,digits)]
​
        # appending items of list1 to list2 structure
        index = 0
        counter = 0
        for digit in list1:
            list2[index].append(digit)
            counter += 1
            if counter % len(keyword) == 0:
                index +=1
​
        print("Printing List1: ")
        print(list2)
        print("=" * 20)
​
​
        #check last list length
        length_list = len(list2[-1])
        if length_list != len(keyword):
            adds = len(keyword) - length_list
            while adds > 0:
                list2[-1].append("x")
                adds -= 1
​
        #create dictionary for keyword
        keyword_list = [i for i in keyword]
        keyword_dict = {}
        keyword_dict = {i:keyword_list.index(i) for i in keyword}
        print(keyword_dict)
​
        # iterate through list2 and add the correct
        answer = ""
        sorted_keyword_list = sorted([i for i in keyword])
        print(sorted_keyword_list)
​
​
        column_counter = 0
        row_counter = 0
        for i in range(0, (len(list2) * len(keyword))):
            answer += list2[row_counter][keyword_dict.get(sorted_keyword_list[column_counter])]
            row_counter +=1
            if row_counter == len(list2):
                row_counter = 0
                column_counter += 1
​
        print(answer)
        return answer
​
​
    if msg.find(" ") >= 0:
        answer = encrypt(msg, keyword)
    else:
        answer = decrpyt(msg, keyword)
​
    return answer

