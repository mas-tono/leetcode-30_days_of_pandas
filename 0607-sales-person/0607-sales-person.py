import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    p = pd.merge(orders, company, how='left', on='com_id')
    return sales_person[~sales_person['sales_id'].isin(p[p['name']=='RED']['sales_id'])]['name'].to_frame()