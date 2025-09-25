import pandas as pd

def find_orders_within_range(df, minValue, maxValue):
    # Tổng giá trị từng đơn hàng
    order_totals = df.groupby("OrderID").apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())
    # Lọc đơn hàng trong range
    orders_within_range = order_totals[(order_totals > minValue) & (order_totals < maxValue)]
    # Danh sách các mã đơn hàng không trùng nhau
    unique_orders = df[df['OrderID'].isin(orders_within_range.index)]['OrderID'].drop_duplicates().tolist()
    return unique_orders

df = pd.read_csv("../dataset/SalesTransactions/SalesTransactions.csv")

minValue = float(input("Enter the minimum price: "))
maxValue = float(input("Enter the maximum price: "))
result = find_orders_within_range(df, minValue, maxValue)
print(f"Danh sách các hóa đơn trong phạm vi giá trị từ {minValue} tới {maxValue}: {result}")

