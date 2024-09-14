import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time']-employees['in_time']
    employees.rename(columns={'event_day':'day'}, inplace=True)
    return employees[['day', 'emp_id', 'total_time']].groupby(['day', 'emp_id'], as_index=False).sum().sort_values(['emp_id'])