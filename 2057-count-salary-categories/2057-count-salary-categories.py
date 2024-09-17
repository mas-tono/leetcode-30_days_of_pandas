import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts['stat'] = accounts['income'].apply(lambda x: 'Low Salary' if x<20000 else 'Average Salary' if 20000<=x<=50000 else 'High Salary')
    data=['Low Salary', 'Average Salary', 'High Salary']
    status = pd.DataFrame(data, columns=['stat'])      
    ss = pd.merge(accounts, status, how='right', on='stat')
    return ss.groupby('stat')['account_id'].agg([('accounts_count', 'count')]).reset_index().rename(columns={'stat':'category'})