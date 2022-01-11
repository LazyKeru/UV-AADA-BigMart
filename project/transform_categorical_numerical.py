import pandas as pd

def transform_categorical_numerical(df,id,target):
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
            """
            i=0
            new_tags={}
            for tag in tags:
                new_tags[tag]=i
                i=i+1
                pass
            print(df.loc[df[feature]])
            for id,row in df.loc[feature]:
                df.loc[id,feature] = new_tags[df[row,feature]]
                pass
            """
        pass
    return df
