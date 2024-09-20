import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    f = pd.merge(employee, department, left_on='departmentId', right_on='id', how='left')
    f['rnk'] = f.groupby('departmentId')['salary'].rank(method='dense', ascending=False)
    return f[f['rnk'] == 1][['name_y', 'name_x', 'salary']].rename(columns={'name_y':'Department','name_x':'Employee', 'salary': 'Salary' })