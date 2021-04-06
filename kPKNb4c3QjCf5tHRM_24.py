
def total_sales(sales_table, product):
    lst = []
    product_name = sales_table[0]
    sales = sales_table[1:]
    if product in sales_table[0]:
        for x in range(len(sales)):
            ind = sales_table[0].index(product)
            lst.append(sales[x][ind])
        return sum(lst)
    return "Product not found"

