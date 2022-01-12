import pandas as pd

def transform_categorical_numerical_old(df,id,target):
    """
    transform the categorical colums to numerical. Could have used LabelEncoder()
    :param df df: dataframe we want to extract the information from
    :param string target: name of the models identifier target.
    :param string target: name of the models final target.
    :return: df transformed dataframe
    """
    print("Starting transform from categorical to numerical")
    features=[col for col in df.columns if (col!=target)&(col!=id)]
    print(f"features: {features}")
    for feature in features:
        if df[feature].dtypes == 'object':
            unique = len(df[feature].unique())
            tags = df[feature].unique()
            print(f"Before transforming numerical to categorical {feature} has {unique} unique value : {tags}")
            df[feature] = pd.Categorical(df[feature])
            # Transforms to numerical
            df[feature] = df[feature].cat.codes
            unique = len(df[feature].unique())
            tags = df[feature].unique()
            print(f"After transforming numerical to categorical {feature} has {unique} unique value : {tags}")
        pass
    print("Ending transform from categorical to numerical")
    return df

## comments from the professor
## Could give a bigger weight with the numbers
## from sklearn.preprocessing import LabelEncoder
## get_dummies()
