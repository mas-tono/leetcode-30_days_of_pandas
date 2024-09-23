import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery['check'] = (delivery['order_date'] == delivery['customer_pref_delivery_date'])
    delivery[delivery['check']==True]['check'].count() / delivery['check'].count()
    f = pd.DataFrame({'immediate_percentage':[delivery[delivery['check']==True]['check'].count() * 100 / delivery['check'].count()]})
    return f.round(2)