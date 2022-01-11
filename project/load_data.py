# project/load_data.py

import pandas as pd

def load_data(path):
    data = pd.read_csv(open(path))
    # A few information of the loaded data:
    print(f"""BigMart test loaded data\n\n
    head:\n
    {data.head()}\n
    tail:\n
    {data.tail()}\n
    info:\n
    {data.info()}\n
    checking for missing data:\n
    {data.isnull().sum()}\n
    shape:\n
    {data.shape}\n\n
    """
    )
    return data
