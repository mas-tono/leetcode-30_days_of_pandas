import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    p = employee.groupby('managerId')['managerId'].agg([('hitung','count')]).reset_index()
    p = pd.merge(p, employee, left_on='managerId', right_on='id')
    return p[p['hitung'] >= 5]['name'].to_frame()