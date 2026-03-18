import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salary = accounts[accounts['income'] < 20000]
    average_salary = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)]
    high_salary = accounts[accounts['income'] > 50000]
    return pd.DataFrame({
    'category': ['Low Salary', 'Average Salary', 'High Salary'],
    'accounts_count': [len(low_salary), len(average_salary), len(high_salary)]
})