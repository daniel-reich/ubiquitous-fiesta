
def index_filter(indexes, strings):
    res_list = [strings[i] for i in indexes]
    return ''.join(res_list).lower()

