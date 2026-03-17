import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    new_table = pd.melt(products, id_vars='product_id', var_name='store', value_name='price')
    new_table = new_table.dropna()
    return new_table