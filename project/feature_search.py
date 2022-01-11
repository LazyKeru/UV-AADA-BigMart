# Data Analysis

# I already now the name for each rows
# Item_Identifier	Item_Weight	Item_Fat_Content	Item_Visibility	Item_Type
# Item_MRP	Outlet_Identifier	Outlet_Establishment_Year	Outlet_Size	Outlet_Location_Type
# Outlet_Type	Item_Outlet_Sales

def feature_search(df):
    for column in df.columns:
        print(f"{column} has {len(df[column].unique())} unique value : {df[column].unique()}")
        pass
    print(f"Describe our dataframe:\n{df.describe()}")
    pass
