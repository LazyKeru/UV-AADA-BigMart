import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def explore_categorical_features(df,cat_features,target):
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
