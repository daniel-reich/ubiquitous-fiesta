
def return_end_of_number(num):
    num = str(num)
    return num+ ("-TH" if "11"<=num[-2:]<="13" or num[-1] not in "123" \
    else ["-ST","-ND","-RD"][int(num[-1])-1])

