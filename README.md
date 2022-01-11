# UV-AADA-BigMart

(regression)

Prédiction des ventes

(feature categorique et feature numérique)

qu'est ce r2 + rmse

## Function :

### load_data observation

#### Test

Size: (5681 rows * 11 columns)
Has missing data (976 for Item_weight, 1606 for Outlet_Size)

#### Train

Size: (8523 rows * 12 columns)
Has missing data (1463 for Item_weight, 2410 for Outlet_Size)

### feature_search observation

#### Test

#### Train
- Item_Identifier has 1559 unique value : ['FDA15' 'DRC01' 'FDN15' ... 'NCF55' 'NCW30' 'NCW05']
- Item_Weight has 416 unique value : [ 9.3    5.92  17.5 ... 5.21   5.4 ]

###

### regression_selection obtained results

Best params for each regressor

best_params_ for KNeighborsRegressor regressor
{'leaf_size': 15, 'n_neighbors': 9, 'weights': 'distance'}
best_score_ for KNeighborsRegressor regressor: 0.48036216829262707
R2 for KNeighborsRegressor best_score_ regressor: 0.5222367940146722
RMSE for KNeighborsRegressor best_score_ regressor: 1178.882890821993

best_params_ for RandomForestRegressor regressor
{'max_depth': None, 'max_features': 'auto', 'min_samples_leaf': 100, 'n_estimators': 400, 'n_jobs': 4, 'random_state': 0}
best_score_ for RandomForestRegressor regressor
0.5840023775597037
R2 for RandomForestRegressor best_score_ regressor: 0.5996242744010539
RMSE for RandomForestRegressor best_score_ regressor: 1079.1906748781348

best_params_ for CatBoostRegressor regressor
{'depth': 3, 'iterations': 100, 'learning_rate': 0.1, 'loss_function': 'RMSE'}
best_score_ for CatBoostRegressor regressor
0.5976648644070012
R2 for CatBoostRegressor best_score_ regressor: 0.6121388256861613
RMSE for CatBoostRegressor best_score_ regressor: 1062.1906364309425

best_params_ for GradientBoostingRegressor regressor
{'learning_rate': 0.03, 'max_depth': 4, 'n_estimators': 100, 'subsample': 0.5}
best_score_ for GradientBoostingRegressor regressor
0.5936869547812392
R2 for GradientBoostingRegressor best_score_ regressor: 0.6039579299923228
RMSE for GradientBoostingRegressor best_score_ regressor: 1073.3342194804886

best_params_ for DecisionTreeRegressor regressor
{'max_depth': 8, 'min_samples_leaf': 100}
best_score_ for DecisionTreeRegressor regressor
0.5825088678155786
R2 for DecisionTreeRegressor best_score_ regressor: 0.5961359345526586
RMSE for DecisionTreeRegressor best_score_ regressor: 1083.8817927869181

best_params_ for XGBRegressor regressor
{'learning_rate': 0.01, 'max_depth': 3, 'n_estimators': 500, 'n_jobs': 4}
best_score_ for XGBRegressor regressor
0.5958467441412338
R2 for XGBRegressor best_score_ regressor: 0.6090278050443259
RMSE for XGBRegressor best_score_ regressor: 1066.442024998566

best_params_ for LinearRegression regressor
{'normalize': True}
best_score_ for LinearRegression regressor
0.5069807272751782
R2 for LinearRegression best_score_ regressor: 0.512151655514078
RMSE for LinearRegression best_score_ regressor: 1191.2604747445223

best_params_ for Ridge regressor
{'alpha': 0.05, 'normalize': True}
best_score_ for Ridge regressor
0.5054256927204294
R2 for Ridge best_score_ regressor: 0.5104172373734344
RMSE for Ridge best_score_ regressor: 1193.3762046108932

## workflows

### semantic-version

[![semantic-version](https://img.shields.io/github/workflow/status/LazyKeru/UV-AADA-projet-apprentissage-automatique/Semantic-version?style=plastic)](https://github.com/LazyKeru/UV-AADA-BigMart/actions/workflows/semantic-versioning.yml)

### Run Python Tests
[![Run Python Tests](https://img.shields.io/github/workflow/status/LazyKeru/UV-AADA-projet-apprentissage-automatique/Semantic-version?style=plastic)](https://github.com/LazyKeru/UV-AADA-BigMart/actions/workflows/python-tests.yml)
#### test are runned for:
- ./project/function/load_data module with ./tests/test_load_data
- ./project/function/feature_extraction with ./tests/test_feature_extraction.py

## Commit convention :
- build: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
- ci: Changes to our CI configuration files and scripts (examples: CircleCi, SauceLabs)
- docs: Documentation only changes
- feat: A new feature
- fix: A bug fix
- perf: A code change that improves performance
- refactor: A code change that neither fixes a bug nor adds a feature
- test: Adding missing tests or correcting existing tests
