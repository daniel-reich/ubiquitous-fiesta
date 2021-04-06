
def decrypt(lst):
    abet = list("abcdefghijklmnopqrstuvwxyz")
    nums = []
    for i in abet:
        nums.append(abet.index(i)+1)
    for n in lst:
        nums.remove(n)
    x = nums[0] - 1
    let = abet[x]
    let = let.upper()
    return(let)

