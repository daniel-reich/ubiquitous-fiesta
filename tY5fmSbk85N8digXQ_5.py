
def ones_infection(arr):
    return MarkRowsColsWith1s(arr).get_results()
​
​
class MarkRowsColsWith1s():
    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)
        self.width = len(arr[0])
        self.row_with_1=set()
        self.col_with_1 = set()
​
    def get_rows_cols_with_1s(self):
​
        for row in range (self.length):
            for col in range(self.width):
                if self.arr[row][col]==1:
                    self.row_with_1.add(row)
                    self.col_with_1.add(col)
​
    def set_1s (self):
​
        for row in range(self.length):
            if row in self.row_with_1:
                self.arr[row] = [1]*self.width
                continue
            for col in self.col_with_1:
                self.arr[row][col]=1
​
    def get_results(self):
        self.get_rows_cols_with_1s()
        self.set_1s()
        return self.arr

