def split_categorical_numerical(df, target):
    """
    Prints information about the numerical features. That we will analyse in function of the target
    :param DataFrame df: dataframe we want to get information about
    :param array num_features: array of all the num_features name
    :param string target: name of the model final target.
    :return:
    """
    print("starting splitting categorical numerical")
    features=[col for col in df.columns if col!=target]
    categorical_df=list(df[features].select_dtypes(include='object').columns)
    numerical_df=list(set(features)-set(categorical_df))
    print(f"categorical features {len(categorical_df)} : {categorical_df}")
    print(f"numerical features {len(numerical_df)} : {numerical_df}")
    print("ending splitting categorical numerical")
    return categorical_df, numerical_df
