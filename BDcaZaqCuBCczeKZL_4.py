
def arrow(num):
    half = [">" * i for i in range(1, num + 1)]
    return half + half[-2::-1] if num % 2 else half + half[::-1]

