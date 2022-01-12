# classifier_parameters_selection
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.feature_selection import RFECV
from sklearn.pipeline import Pipeline
# to add more parameters to the default classifier
import numpy as np
# classifiers, remove if your remove default
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from catboost import CatBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from .analyse import analyse

default_names = [
    #"LogisticRegression", # Neural network models
    #"KNeighborsRegressor",
    "RandomForestRegressor",
    "CatBoostRegressor",
    "GradientBoostingRegressor",
    "DecisionTreeRegressor",
    "XGBRegressor",
    "LinearRegression",
    "Ridge"
]

default_classifiers = [
    #LogisticRegression(),
    #KNeighborsRegressor(),
    RandomForestRegressor(),
    CatBoostRegressor(),
    GradientBoostingRegressor(),
    DecisionTreeRegressor(),
    XGBRegressor(),
    LinearRegression(),
    Ridge()
]

default_parameters = [
    #{
    #    'penalty':['l1', 'l2', 'elasticnet'],        # l1 is Lasso, l2 is Ridge
    #    'solver':['liblinear'],
    #    'C': np.linspace(0.00002,1,100)
    #},
    #{
    #    'weights': ['uniform', 'distance'],
    #    'n_neighbors': [3, 5, 7, 9],
    #    'leaf_size': [15, 20],
    #    # Many more config : https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
    #},
    {
        'n_estimators': [100, 200, 400, 1000],
        'max_features': ["auto", "log2"],
        'max_depth': [None, 5, 6],
        'min_samples_leaf': [100],
        'n_jobs': [4, 5],
        'random_state': [0]
        # Many more config : https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
    },
    {
        'iterations': [50, 100, 150, 200, 300],
        'depth': [3],
        'learning_rate': [0.1],
        'loss_function': ['RMSE']
        # Many more config : https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
    },
    {
        'learning_rate': [0.01,0.02,0.03,0.04],
        'subsample'    : [0.9, 0.5, 0.2, 0.1],
        'n_estimators' : [100,500,1000, 1500],
        'max_depth'    : [4,6,8,10]
    },
    {
        'max_depth': [8, 16, 30],
        'min_samples_leaf'    : [100, 150, 200]
    },
    {
        'n_estimators': [50,100,200,500,1000],  # this parameter means using the GPU when training our model to speedup the training process
        'max_depth': [3,5,7,9],
        'n_jobs': [4],
        'learning_rate': [0.001,0.01,0.02,0.05,0.1],
    },
    {
        'normalize': [True]
    },
    {
        'alpha': [0.05, 0.1],
        'normalize': [True]
    }

]

def regression_and_features_selection(df, target, names=default_names,classifiers=default_classifiers,parameters=default_parameters):
    """
    Exhaustive search over specified parameters for a large pannel of regressor and selecting features
    :param dataframe df: the data that we will split using train_test_split() for training
    :param array names: the names of the regressors
    :param array classifiers: the function of the regressors
    :param array parameters: the parameters of the regressors
    :return: it returns the best obtained regressor model
    """
    #splitting data
    features=[col for col in df.columns if col!=target]
    x_train, x_test, y_train, y_test = train_test_split(
        df[features],
        df[target],
        test_size=0.3,
        random_state=1)
    regs = {}
    for name, classifier, parameter in zip(names, classifiers, parameters):
        print(f"Start GridSearchCV for {name} classifier")
        # Recursive Feature Elimination
        rfecv  = RFECV(estimator=classifier, step=1, cv=5)
        #Exhaustive search over specified parameter for a specific classifier
        reg = GridSearchCV(classifier, parameter, scoring='r2', n_jobs=-1, cv=3)
        pipeline  = Pipeline([('feature_sele',rfecv),('reg_cv',reg)])
        pipeline.fit(x_train, y_train)
        pipeline.predict(x_test)
        print(f"End GridSearchCV for {name} classifier")
        regs[name] = pipeline
        pass
    # sent to analyse function
    """
    for name, reg in regs.items():
        print(f"best_params_ for {name} classifier\n{reg.best_params_}")
        print(f"best_score_ for {name} classifier\n{reg.best_score_}")
        print(f'R2 for {name}: {r2_score(y_test, reg.best_estimator_.predict(x_test))}')
        print(f'RMSE for {name}: {np.sqrt((mean_squared_error(y_test, reg.best_estimator_.predict(x_test))))}')
        pass
    """
    best_score=0
    for name, reg in regs.items():
        if best_score < reg.score(x_test, y_test):
            best_score = reg.score(x_test, y_test)
            print(f"{name}: {best_score}")
            best_reg = reg
            pass
        pass
    pass
    return best_reg
