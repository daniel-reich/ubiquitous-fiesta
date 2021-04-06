
def total_sales(sales_table, product):
    if product not in sales_table[0]:
        return 'Product not found'
    ind=sales_table[0].index(product)
    return sum(sales_table[each][ind] for each in range(1,len(sales_table) ))

