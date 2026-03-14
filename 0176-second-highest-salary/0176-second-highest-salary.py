import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sec_salary = employee['salary'].drop_duplicates().sort_values(ascending=False)
    result = sec_salary.iloc[1] if len(sec_salary) >= 2 else None
    return pd.DataFrame({'SecondHighestSalary': [result]})