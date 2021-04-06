
def title_to_number(s):
    values = [ord(i) - 64 for i in s]
    ans = [i for i in range(len(values))][::-1]
    return sum(i * 26 ** j for i,j in zip(values,ans))

