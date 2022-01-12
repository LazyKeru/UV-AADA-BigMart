import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def explore_categorical_features(df,cat_features,target):
    """
    Prints information about the categorical features. That we will analyse in function of the target
    :param DataFrame df: dataframe we want to get information about
    :param array cat_features: array of all the cat_features name
    :param string target: name of the model final target (we don't want to change it)
    :return:
    """
    for feature in cat_features:
        print(f"{feature} has {len(df[feature].unique())} unique value : {df[feature].unique()}")
        if (len(df[feature].unique())) < 15:
            plt.figure()
            df[[feature, target]].groupby(feature).median().plot(kind='bar')
        else:
            plt.figure()
            df[[feature, target]].groupby(feature).median().plot(kind='barh')
            pass
        pass
    plt.show()
    pass
