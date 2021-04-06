
size = 5000
A = list(range(1, size + 1))
kill = 2
while True:
    A = [A[i] for i in range(len(A)) if (i + 1) % kill != 0]
    kill += 1
    while kill not in A and kill < A[-1]:
        kill += 1
    if kill > A[-1]:
        break
​
def get_lucky_number(size, nth):
    return A[nth - 1]

