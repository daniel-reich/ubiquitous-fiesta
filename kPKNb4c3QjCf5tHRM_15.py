
def total_sales(sales_table, product):
        try:
            return sum([list(x) for x in zip(*sales_table[1:])][sales_table[0].index(product)])
        except:
            return "Product not found"

