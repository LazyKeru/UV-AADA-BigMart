# tests/main_regression_selection

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import project as proj

path_test = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset/Test.csv'))
path_train = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset/Train.csv'))

target='Item_Outlet_Sales'
identifier= 'Item_Identifier'

def main_regression_selection():
    train = proj.load_data(path_train)
    test = proj.load_data(path_test)
    train = proj.df_uniform_categorical(train,'Item_Fat_Content',{'low fat':'Low Fat','LF':'Low Fat','reg':'Regular'})
    print(train)
    categorical_f, numerical_f = proj.split_categorical_numerical(train, target)
    train = proj.df_preprocessing_num_features(train, numerical_f)
    print(train)
    train = proj.transform_categorical_numerical_old(train, target, identifier)
    print(train)
    train = train.drop([identifier], axis=1)
    print(train)
    proj.regression_selection(train, target)
    pass


main_regression_selection()
