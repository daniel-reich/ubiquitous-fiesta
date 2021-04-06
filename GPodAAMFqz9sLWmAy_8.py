
#edabit
#odd_even
​
def one_odd_one_even(num):
    num_string = str(num)
    int_1 = int(num_string[0])
    int_2 = int(num_string[-1])
    if (int_1 % 2 == 0 and int_2 % 2 != 0) or (int_1 % 2 != 0 and int_2 % 2 == 0):
        return True
    else:
        return False
​
def main():
    pass
​
if __name__ == "__main__":
    main()

