def split_categorical_numerical(df, target):
    features=[col for col in df.columns if col!=target]
    categorical_df=list(df[features].select_dtypes(include='object').columns)
    numerical_df=list(set(features)-set(categorical_df))
    print(f"categorical features {len(categorical_df)} : {categorical_df}")
    print(f"numerical features {len(numerical_df)} : {numerical_df}")
    return categorical_df, numerical_df
