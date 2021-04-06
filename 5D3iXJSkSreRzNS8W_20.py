
def news_at_ten(txt, n):
    pass
    message = ' ' * n + txt + ' ' * n
    begin = 0
    end = n
    list_message = []
    while end <= len(message):
        list_message.append(message[begin:end])
        begin += 1
        end += 1
    return list_message

