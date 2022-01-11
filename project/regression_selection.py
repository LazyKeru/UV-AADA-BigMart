# classifier_parameters_selection
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
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
    "KNeighborsRegressor",
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
    KNeighborsRegressor(),
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
    {
        'weights': ['uniform', 'distance'],
        'n_neighbors': [3, 5, 7, 9],
        'leaf_size': [15, 20],
        # Many more config : https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
    },
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

def regression_selection(df, target, names=default_names,classifiers=default_classifiers,parameters=default_parameters):
    """
    Exhaustive search over specified parameters for a large pannel of classifier
    :param dataframe x_train: the data to train the model
    :param dataframe x_test: the data to test the model
    :param dataframe y_train: the labels of the data to train the model
    :param dataframe y_train: the labels of the data to test the model
    :param array names: the names of the classifiers
    :param array classifiers: the function of the classifiers
    :param array parameters: the parameters of the classifiers
    :return: it returns the prediction
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
        #Exhaustive search over specified parameter for a specific classifier
        reg = GridSearchCV(classifier, parameter, scoring='r2', n_jobs=-1, cv=3)
        reg.fit(x_train, y_train)
        reg.predict(x_test)
        print(f"End GridSearchCV for {name} classifier")
        regs[name] = reg
        pass
    # sent to analyse function
    """
    for name, reg in regs.items():
        print(f"best_params_ for {name} classifier\n{reg.best_params_}")
        print(f"best_score_ for {name} classifier\n{reg.best_score_}")
        print(f'R2 for {name}: {r2_score(y_test, reg.best_estimator_.predict(x_test))}')
        print(f'RMSE for {name}: {np.sqrt((mean_squared_error(y_test, reg.best_estimator_.predict(x_test))))}')
        pass
    best_score=0
    for name, reg in regs.items():
        if best_score < reg.best_score_:
            best_score = reg.best_score_
            best_reg = reg.best_estimator_
            pass
        pass
    pass
    """
    analyse(regs, x_test, y_test)
    return regs
