import pandas as pd

# join customers & orders -> filtering join
# rename column
# extract the column

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return customers[~customers.id.isin(orders.customerId)].rename(columns={'name':'Customers'})[['Customers']]