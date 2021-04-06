
VALUES = {chr(65+i): i+1 for i in range(26)}
for i in range(10):
    VALUES[str(i)] = i
INV_VALUES = {value: key for key, value in VALUES.items()}
​
POWERS = {(base, power): base**power for base in range(1, 37) for power in range(200)}
​
​
def from_base(k, base_k):
    # convert integer k in base base_k to decimal (base 10)
    L = len(k)
    res = 0
    for i in range(L - 1, -1, -1):
        res += VALUES[k[i]] * POWERS[(base_k, L - 1 - i)]
    return res
​
def title_to_number(s):
  return from_base(s, 26)

