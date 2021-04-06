
def total_sales(sales_table, product):
    i=sales_table[0].index(product) if product in sales_table[0] else -1
    return sum(j[i] for j in sales_table[1:]) if i!=-1 else 'Product not found'

