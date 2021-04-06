
#edabit
#list of prime numbers
​
def all_prime(lst):
    result = True
    for num in lst:
        if num == 1:
            result = False
            break
        else:
            for i in range(2,num):
                if num % i == 0:
                    result = False
                    break
    return result
​
def main():
    pass
​
if __name__ == "__main__":
    main()

