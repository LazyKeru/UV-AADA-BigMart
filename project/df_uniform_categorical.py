def df_uniform_categorical(df,feature,code):
    print(f"Uniforming the categorical {feature}")
    df.replace({feature:code},inplace=True)
    return df
