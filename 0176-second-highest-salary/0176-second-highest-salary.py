import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates('salary', keep='first', inplace=True)
    employee['rnk'] = employee['salary'].rank(ascending=False)
    p = employee[employee['rnk']==2]['salary'].to_frame()
    p.rename(columns={'salary':'SecondHighestSalary'}, inplace=True)
    if p.empty:
        p = pd.DataFrame({'SecondHighestSalary':[None]})
    
    return p