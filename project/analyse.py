from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import numpy as np

def analyse(regs):
    print("Best params for each regressor")
    for name, reg in regs.items():
        print(f"best_params_ for {name} regressor\n{reg.best_params_}")
        print(f"best_score_ for {name} regressor\n{reg.best_score_}")
        print(f'R2 for {name} best_score_ regressor: {r2_score(y_test, reg.best_score_.predict(x_test))}')
        print(f'RMSE for {name} best_score_ regressor: {np.sqrt((mean_squared_error(y_test, reg.best_score_.predict(x_test))))}')
        pass
