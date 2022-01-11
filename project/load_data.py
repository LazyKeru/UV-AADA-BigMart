# project/load_data.py

import pandas as pd

def load_data(path_test, path_train):
    BigMart_test = pd.read_csv(open(path_test))
    BigMart_train = pd.read_csv(open(path_train))
    # A few information of the loaded test data:
    print(f"""BigMart test loaded data\n\n
    head:\n
    {BigMart_test.head()}\n
    tail:\n
    {BigMart_test.tail()}\n
    info:\n
    {BigMart_test.info()}\n
    checking for missing data:\n
    {BigMart_test.isnull().sum()}
    """
    )
    # A few information of the loaded train data:
    print(f"""BigMart train loaded data\n\n
    head:\n
    {BigMart_train.head()}\n
    tail:\n
    {BigMart_train.tail()}\n
    info:\n
    {BigMart_train.info()}\n
    checking for missing data:\n
    {BigMart_train.isnull().sum()}
    """
    )
    pass
