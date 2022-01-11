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
    # 'Item_Fat_Content' has multiple tags for the same category
    train = proj.df_uniform_categorical(train,'Item_Fat_Content',{'low fat':'Low Fat','LF':'Low Fat','reg':'Regular'})
    print(f"head: {train.head()}")
    ## Local var
    #print("transform categorical to numercial for train")
    #train=proj.transform_categorical_numerical(train,'Item_Identifier','Item_Outlet_Sales')
    #print("transform categorical to numercial for test")
    #test=proj.transform_categorical_numerical(test,'Item_Identifier','Item_Outlet_Sales')
    categorical_f, numerical_f = proj.split_categorical_numerical(train, target)
    #proj.explore_numerical_features(train, numerical_f, target)
    #proj.explore_categorical_features(train, categorical_f, target)
    train = proj.df_preprocessing_num_features(train, numerical_f)
    print(f"head: {train.head()}")
    train = proj.transform_categorical_numerical(train, categorical_f)
    print(f"head: {train.head()}")
    pass


test_feature_extraction()
