# tests/load_data

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import project as proj

path_train = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset/Test.csv'))
path_test = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'dataset/Train.csv'))
# workflow
def test_load_data():
    train, test = proj.load_data(path_test, path_train)
    return train, test

print(test_load_data())
