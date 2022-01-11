import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def explore_numerical_features(df,num_features,target):
    plt.figure(figsize=(14,7))
    corr = df[num_features+[target]].corr()
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(240,10,as_cmap=True),
                square=True)
    plt.figure()
    plt.scatter(x=df['Item_MRP'], y=df[target])
    plt.xlabel("Item_MRP")
    plt.ylabel("Item_Ou<tlet_Sales")
    sns.scatterplot(x=df['Item_MRP'], y=df[target])
    plt.xlabel("Item_MRP")
    plt.ylabel("Item_Outlet_Sales")
    plt.figure()
    sns.displot(df[target],color="purple")
    plt.show()
    print("the skew (is positive):",df[target].skew())
    pass
