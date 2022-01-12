# Data Analysis

# I already now the name for each rows
# Item_Identifier	Item_Weight	Item_Fat_Content	Item_Visibility	Item_Type
# Item_MRP	Outlet_Identifier	Outlet_Establishment_Year	Outlet_Size	Outlet_Location_Type
# Outlet_Type	Item_Outlet_Sales

#the function which get the columns which contains the null values
# credit: https://www.kaggle.com/aichatoutoure/bigmart-sales-predictions
def get_null_cols(X,cols):
    """
    Prints information about the percentage of nulls
    :param DataFrame X: dataframe we want to get information about the percentage of nulls
    :param array cols: string of all the columns name
    :return:
    """
    null_cols=list(X[cols].isnull().sum()[X[cols].isnull().sum()>0].index)
    print("columns which contains null",null_cols)
    for col in null_cols :
        percent=(X[col].isnull().sum()/len(X[cols]))*100
        print("We have ",round(percent,2)," % to nulls values for ",col,"column")

def feature_search(df):
    """
    Describes the dataframe.
    :param DataFrame df: dataframe of the csv file
    :return:
    """
    for column in df.columns:
        print(f"{column} has {len(df[column].unique())} unique value : {df[column].unique()}")
        pass
    print(f"Describe our dataframe:\n{df.describe()}")
    features=[col for col in df.columns]
    get_null_cols(df,features)
    pass
