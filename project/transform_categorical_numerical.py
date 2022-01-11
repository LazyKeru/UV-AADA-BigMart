from sklearn.preprocessing import LabelEncoder

def transform_categorical_numerical(df, cate_features):
    print("Starting transform from categorical to numerical")
    for feature in cate_features:
        print(feature)
        encoder=LabelEncoder()
        df[feature]=encoder.fit_transform(df[feature])
    print("Ending transform from categorical to numerical")
