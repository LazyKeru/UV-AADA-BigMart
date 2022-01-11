# tests/load_data

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import project as proj

path_test = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset/Test.csv'))
path_train = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset/Train.csv'))
# workflow
def test_load_data():
    train = proj.load_data(path_train)
    test = proj.load_data(path_test)
    return test, train

def test_feature_extraction():
    test, train = test_load_data()
    proj.feature_search(train)
    new=proj.transform_categorical_numerical(train,'Item_Identifier','Item_Outlet_Sales')
    pass


test_feature_extraction()
