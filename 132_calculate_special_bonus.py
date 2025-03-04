# Create new column 'bonus' with if else condition such that 'bonus' == 'salary' if employee_id is even
# and the 'name' does not start with M. Sort the resulting df and return in ascending order of id.

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x: x['salary'] if x['employee_id']%2 and not \
                                         x['name'].startswith('M') else 0, axis=1)
    return employees[['employee_id', 'bonus']].sort_values(by=['employee_id'])