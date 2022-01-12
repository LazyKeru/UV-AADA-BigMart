def df_uniform_categorical(df,feature,code):
    """
    Uniforming the tags of a categorical feature colum.
    :param dataframe df: dataframe we want to reformat
    :param string feature: name of the feature we want to uniform
    :param array code: new nomenclature
    :return: df transformed dataframe
    """
    print(f"Uniforming the categorical {feature}")
    df.replace({feature:code},inplace=True)
    return df
