import skleanrn


X_train, X_valid, y_train, y_valid = train_test_split(df[features], df[target], test_size=0.3, random_state=1)
