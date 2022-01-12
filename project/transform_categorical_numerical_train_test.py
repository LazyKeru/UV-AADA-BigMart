import pandas as pd
from sklearn import preprocessing

def transform_categorical_numerical_train_test(df_train, df_test, id, target):
    """
    transform the categorical colums to numerical for the df_test and df_train.
    using LabelEncoder().
    :param dataframe df_train: dataframe we want to reformat
    :param dataframe df_test: dataframe we want to reformat
    :param string id: name of the models identifier target.
    :param string target: name of the models final target.
    :return: df_train, df_test transformed dataframes
    """
    print("Starting transform from categorical to numerical")
    features=[col for col in df_train.columns if (col!=target)&(col!=id)]
    print(f"features: {features}")
    for feature in features:
        if df_train[feature].dtypes == 'object':
            # prepare encoder
            encoder = preprocessing.LabelEncoder()
            encoder.fit(df_train[feature])
            # Transforms train feature to numerical
            df_train[feature] = encoder.transform(df_train[feature])
            # Transforms test feature to numerical
            df_test[feature] = encoder.transform(df_test[feature])
        pass
    print("Ending transform from categorical to numerical")
    return df_train, df_test

def old(df_train, df_test, id, target):
    """
    transform the categorical colums to numerical for the df_test and df_train. Could have used LabelEncoder()
    :param dataframe df_train: dataframe we want to reformat
    :param dataframe df_test: dataframe we want to reformat
    :param string id: name of the models identifier target.
    :param string target: name of the models final target.
    :return: df_train, df_test transformed dataframes
    """
    print("Starting transform from categorical to numerical")
    features=[col for col in df_train.columns if (col!=target)&(col!=id)]
    print(f"features: {features}")
    for feature in features:
        if df_train[feature].dtypes == 'object':
            unique = len(df_train[feature].unique())
            tags = df_train[feature].unique()
            print(f"Before transforming numerical to categorical {feature} has {unique} unique value : {tags}")
            df_train[feature] = pd.Categorical(df_train[feature])
            #preparing dictionnary for df_test
            d = dict(enumerate(df_train[feature].cat.categories))
            d = {a: b for b, a in d.items()}
            print("dictionnary", d)
            # Transforms to numerical
            df_train[feature] = df_train[feature].cat.codes
            unique = len(df_train[feature].unique())
            tags = df_train[feature].unique()
            # transforming df test
            df_test[feature] = pd.Categorical(df_test[feature])
            print(df_test[feature])
            df_test[feature] = df_test[feature].map(d)
            print(df_test[feature])
            print(f"After transforming numerical to categorical {feature} has {unique} unique value : {tags}")
        pass
    print("Ending transform from categorical to numerical")
    return df_train, df_test

## comments from the professor
## Could give a bigger weight with the numbers
## from sklearn.preprocessing import LabelEncoder
## get_dummies()
