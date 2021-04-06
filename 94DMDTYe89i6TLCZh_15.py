
def get_languages(num):
    bin_lst = str(bin(num)[::-1])[:-2]
    lang_lst = ['C#', 'C++', 'Java', 'JavaScript', 'PHP', 'Python', 'Ruby', 'Swift']
    return [lang_lst[int(n)+i-1] for i, n in enumerate(bin_lst) if n=='1']

