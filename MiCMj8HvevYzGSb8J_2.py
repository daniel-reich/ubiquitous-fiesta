
def fibo_word(n):
    if n < 2: return "invalid"
    lst = ["b","a"]; string = ""
    for i in range(n-2): string += lst[i+1] + lst[i]; lst.append(string); string = ""
    return ", ".join(lst)

