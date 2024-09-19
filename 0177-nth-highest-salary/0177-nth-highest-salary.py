import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    
    employee.drop_duplicates('salary', keep='first', inplace=True)
    employee['rnk'] = employee['salary'].rank(ascending=False)
    p = employee[employee['rnk']==N]['salary'].to_frame()
    p.rename(columns={'salary':'getNthHighestSalary'+'('+str(N)+')'}, inplace=True)
    if p.empty:
        p = pd.DataFrame({'getNthHighestSalary'+'('+str(N)+')':[None]})
    
    return p
    
