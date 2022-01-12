# tests/load_data

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import project as proj
from joblib import dump

path_test = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset/Test.csv'))
path_train = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset/Train.csv'))
model_path = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'tests/models/model_bis.pkl'))
dataset_train_path = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'tests/treated_dataset/train_bis.cvs'))
dataset_test_path = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'tests/treated_dataset/test_bis.cvs'))

target='Item_Outlet_Sales'
identifier= 'Item_Identifier'

# workflow
def test_load_data():
    train = proj.load_data(path_train)
    test = proj.load_data(path_test)
    return test, train

def test_feature_extraction():
    train = proj.load_data(path_train)
    test = proj.load_data(path_test)
    print("feature search for train")
    proj.feature_search(train)
    # 'Item_Fat_Content' has multiple tags for the same category
    train = proj.df_uniform_categorical(train,'Item_Fat_Content',{'low fat':'Low Fat','LF':'Low Fat','reg':'Regular'})
    print(train)
    test = proj.df_uniform_categorical(test,'Item_Fat_Content',{'low fat':'Low Fat','LF':'Low Fat','reg':'Regular'})
    print(test)
    ## Local var
    #print("transform categorical to numercial for train")
    #train=proj.transform_categorical_numerical(train,'Item_Identifier','Item_Outlet_Sales')
    #print("transform categorical to numercial for test")
    #test=proj.transform_categorical_numerical(test,'Item_Identifier','Item_Outlet_Sales')
    categorical_f, numerical_f = proj.split_categorical_numerical(train, target)
    #proj.explore_numerical_features(train, numerical_f, target)
    #proj.explore_categorical_features(train, categorical_f, target)
    train, test = proj.transform_categorical_numerical_train_test(train, test, target, identifier)
    print("ran transform_categorical_numerical_train_test")
    print(train)
    print(test)
    categorical_f, numerical_f = proj.split_categorical_numerical(train, target)
    train, test = proj.df_preprocessing_num_features_train_test(train, test, numerical_f+categorical_f)
    print("ran df_preprocessing_num_features_train_test")
    print(train)
    print(test)
    train = train.drop([identifier], axis=1)
    test = test.drop([identifier], axis=1)
    print("ran drop identifier as we already have an index")
    print(train)
    print(test)
    reg = proj.regression_selection(train, target)
    train.to_csv(dataset_train_path)
    test.to_csv(dataset_test_path)
    dump(reg, model_path)
    pass


test_feature_extraction()
