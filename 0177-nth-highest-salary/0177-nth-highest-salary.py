import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    distinct_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    result = distinct_salaries.iloc[N-1] if 1 <= N <= len(distinct_salaries) else None
    return pd.DataFrame({f'getNthHighestSalary({N})': [result]})