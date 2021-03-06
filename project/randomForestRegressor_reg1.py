from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

def randomForestRegressor_reg1(df,target):
    features=[col for col in df.columns if col!=target]
    X_train, X_valid, y_train, y_valid = train_test_split(
        df[features],
        df[target],
        test_size=0.3,
        random_state=1)
    model = RandomForestRegressor(n_estimators=1000, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    print('R2:', r2_score(y_valid, preds))
    print('RMSE', mean_squared_error(y_valid, preds))
    pass
