import pandas as pd

def find_top3_products(df):
    product_total = df.groupby("ProductID").apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())
    top_products = product_total.sort_values(ascending=False).head(3)
    return top_products.reset_index()

df = pd.read_csv("../dataset/SalesTransactions/SalesTransactions.csv")
result = find_top3_products(df)
print(result)