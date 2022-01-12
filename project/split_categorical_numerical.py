def split_categorical_numerical(df, target):
    """
    Split the categorical and numerical columns names
    :param df df: dataframe we want to extract the information from
    :param string target: name of the models final target.
    :return: string categorical_f, string numerical_f retrun the split categorical and numerical features name
    """
    print("starting splitting categorical numerical")
    features=[col for col in df.columns if col!=target] #remove target from the features
    categorical_f=list(df[features].select_dtypes(include='object').columns)
    numerical_f=list(set(features)-set(categorical_f))
    print(f"categorical features {len(categorical_f)} : {categorical_f}")
    print(f"numerical features {len(numerical_f)} : {numerical_f}")
    print("ending splitting categorical numerical")
    return categorical_f, numerical_f
