import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(department, left_on='departmentId', right_on='id')
    max_salaries = merged.groupby('departmentId')['salary'].transform('max')
    result = merged[merged['salary'] == max_salaries][['name_y', 'name_x', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']
    return result