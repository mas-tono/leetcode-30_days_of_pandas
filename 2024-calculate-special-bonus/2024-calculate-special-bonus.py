import pandas as pd

# the key is to identify first letter of name, extract string
# combine with using lambda function for condition

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x: x['salary'] 
                                               if ((x['employee_id']%2 != 0) & (x['name'][0] != 'M')) 
                                               else 0, axis=1)
    
    return employees[['employee_id', 'bonus']].sort_values(['employee_id'])                                               