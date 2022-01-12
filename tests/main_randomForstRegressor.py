# tests/main_randomForstRegressor

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import project as proj

path_test = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset/Test.csv'))
path_train = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset/Train.csv'))

target='Item_Outlet_Sales'
identifier= 'Item_Identifier'

def main_randomForstRegressor():
    train = proj.load_data(path_train)
    # 'Item_Fat_Content' has multiple tags for the same category
    train = proj.df_uniform_categorical(train,'Item_Fat_Content',{'low fat':'Low Fat','LF':'Low Fat','reg':'Regular'})
    categorical_f, numerical_f = proj.split_categorical_numerical(train, target)
    train = proj.df_preprocessing_num_features(train, numerical_f)
    print(train)
    train = proj.transform_categorical_numerical_old(train, target, identifier)
    print(train)
    # removes the identifier column, as we already have the index to identify each row
    train = train.drop([identifier], axis=1)
    print(train)
    proj.randomForestRegressor_reg1(train,target)
    pass


main_randomForstRegressor()
