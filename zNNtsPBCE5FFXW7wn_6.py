
#edabit
#emptying values
​
def empty_values(lst):
    result = []
    for i in lst:
        if type(i) == int:
            result.append(0)
        elif type(i) == float:
            result.append(0.0)
        elif type(i) == str:
            result.append('')
        elif type(i) == bool:
            result.append(False)
        elif type(i) == list:
            result.append([])
        elif type(i) == tuple:
            result.append(())
        elif type(i) == set:
            result.append(set())
        elif type(i) == type(None):
            result.append(None)
    return result
​
def main():
    pass
​
if __name__ == "__main__":
    main()

