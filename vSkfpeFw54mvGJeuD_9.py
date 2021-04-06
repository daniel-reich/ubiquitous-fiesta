
def isPalindrome(number):
    number = str(number)
    listedNum = list(number)
    listedNum = listedNum[::-1]
    reverseNum = ''.join(listedNum)
    sum = str(int(number) + int(reverseNum))
    listedSum = list(sum)
    listedSum = listedSum[::-1]
    reverseSum = ''.join(listedSum)
    if (reverseSum == sum):
        return True
    else:
        return sum
​
def lychrel(num):
    count = 0
    ans = []
    y = str(num)
    reverse = y[::-1]
    reverseStr = ''.join(reverse)
    if(y != reverseStr):
        while True:
            count = count + 1
            x = isPalindrome(y)
            y = int(x)
            if(x == True):
                break
            if (count > 500):
                count = -1
                break
            else:
                x = isPalindrome(y)
​
    if (count > -1):
        return count
    else:
        return True

