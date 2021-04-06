
#edabit
#bundle up
​
def calc_bundled_temp(n, temperature):
    lst = temperature.split('*')
    temp = int(lst[0])
    for i in range(1,n+1):
        temp += (0.1*temp)
    return '%s*C'%round(temp, 1)
​
def main():
    pass
​
if __name__ == "__main__":
    main()

