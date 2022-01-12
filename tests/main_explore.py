# tests/main_analyse

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import project as proj

path_test = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset/Test.csv'))
path_train = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset/Train.csv'))

target='Item_Outlet_Sales'
identifier= 'Item_Identifier'

def main_analyse():
    # We will only analyse the train dataset, as we will train our model with that csv
    train = proj.load_data(path_train)
    print("feature search for train")
    proj.feature_search(train)
    # we saw that 'Item_Fat_Content' has multiple tags for the same description
    train = proj.df_uniform_categorical(train,'Item_Fat_Content',{'low fat':'Low Fat','LF':'Low Fat','reg':'Regular'})
    print(f"train new dataframe :\n{train}")
    categorical_f, numerical_f = proj.split_categorical_numerical(train, target)
    # Will explore the numerical features
    proj.explore_numerical_features(train, numerical_f, target)
    # Will explore the categorical features
    proj.explore_categorical_features(train, categorical_f, target)

main_analyse()
