# There are null values in two columns Item_Weight and Outlet_Size
def df_preprocessing_num_features_train_test(df_train, df_test, num_features):
    print("starting num feature preprocessing")
    for feature in num_features:
        print(f"{feature} preprocessing")
        df_train[feature].loc[df_train[feature].isnull()] = df_train[feature].mean()
        df_test[feature].loc[df_test[feature].isnull()] = df_train[feature].mean()
        #feature_mean = df[['Item_Identifier', 'Item_Weight']].groupby('Item_Identifier').mean()
        #print(f"{feature_mean}")
        #feature_mean[feature_mean['Item_Weight'].isnull()] = df['Item_Weight'].mean()
        pass
    print("ending num feature preprocessing")
    return df_train, df_test
