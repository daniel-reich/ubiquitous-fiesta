
def total_sales(sales_table, product):
    try:
        return sum(i[sales_table[0].index(product)] for i in sales_table[1:])
    except:
        return "Product not found"

