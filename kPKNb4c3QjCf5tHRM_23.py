
def total_sales(sales_table, product):
    if product not in sales_table[0]:
        return 'Product not found'
    idx = sales_table[0].index(product)
    gh = [x for y in sales_table[1:] for x in y]
    return sum(x for x in gh[idx::len(sales_table[0])])

