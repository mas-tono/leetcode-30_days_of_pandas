import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    cust_cnt = orders.groupby('customer_number')['order_number'].count().reset_index()
    return cust_cnt[cust_cnt['order_number'] == cust_cnt['order_number'].max()][['customer_number']]