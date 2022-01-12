import sys
import os
from joblib import load
import pandas as pd

path_model = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'tests/models/model_main_extract.pkl'))
path_csv = (os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),'tests/treated_dataset/test_main_extract.cvs'))


reg = load(path_model)
csv = pd.read_csv(open(path_csv))

print(reg.predict(csv))
