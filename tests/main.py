# tests/load_data

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import project as proj

path_test = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset/Test.csv'))
path_train = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset/Train.csv'))

target='Item_Outlet_Sales'

# workflow
def test_load_data():
    train = proj.load_data(path_train)
    test = proj.load_data(path_test)
    return test, train

def test_feature_extraction():
    test, train = test_load_data()
    print("feature search for train")
    proj.feature_search(train)
    ## Local var
    #print("transform categorical to numercial for train")
    #train=proj.transform_categorical_numerical(train,'Item_Identifier','Item_Outlet_Sales')
    #print("transform categorical to numercial for test")
    #test=proj.transform_categorical_numerical(test,'Item_Identifier','Item_Outlet_Sales')
    categorical_df, numerical_df = proj.split_categorical_numerical(train, target)
    proj.explore_numerical_features(train, numerical_df, target)
    proj.explore_categorical_features(train, categorical_df, target)
    pass


test_feature_extraction()
