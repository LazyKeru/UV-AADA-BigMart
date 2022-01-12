# tests/load_data

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import project as proj
from joblib import dump

path_test = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset/Test.csv'))
path_train = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset/Train.csv'))
model_path = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'tests/models/model.pkl'))
dataset_train_path = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'tests/treated_dataset/train.cvs'))
dataset_test_path = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'tests/treated_dataset/test.cvs'))

target='Item_Outlet_Sales'
identifier= 'Item_Identifier'

def test_feature_extraction():
    train = proj.load_data(path_train)
    test = proj.load_data(path_test)

    print("Uniforming Item_Fat_Content")
    train = proj.df_uniform_categorical(train,'Item_Fat_Content',{'low fat':'Low Fat','LF':'Low Fat','reg':'Regular'})
    test = proj.df_uniform_categorical(test,'Item_Fat_Content',{'low fat':'Low Fat','LF':'Low Fat','reg':'Regular'})
    print("ran df_uniform_categorical")
    print(f"""
    feature search train:\n
    {proj.feature_search(train)}\n
    feature search test:\n
    {proj.feature_search(test)}
    """)

    # simple split
    categorical_f, numerical_f = proj.split_categorical_numerical(train, target)
    #simple split

    print("preprocessing num features")
    train, test = proj.df_preprocessing_num_features_train_test(train, test, numerical_f)
    print("ran df_preprocessing_num_features_train_test")
    print(f"""
    feature search train:\n
    {proj.feature_search(train)}\n
    feature search test:\n
    {proj.feature_search(test)}
    """)

    print("transforming categorical to  numerical features")
    train, test = proj.transform_categorical_numerical_train_test(train, test, target, identifier)
    print("ran transform_categorical_numerical_train_test")
    print(f"""
    feature search train:\n
    {proj.feature_search(train)}\n
    feature search test:\n
    {proj.feature_search(test)}
    """)
    print("done")



    print("Running drop for the identifier as we already have an index")
    train = train.drop([identifier], axis=1)
    test = test.drop([identifier], axis=1)
    print("feature search train:")
    print(proj.feature_search(train))
    print("feature search test:")
    print(proj.feature_search(test))
    print("done")
    pass


test_feature_extraction()
