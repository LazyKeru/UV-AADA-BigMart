# UV-AADA-BigMart

(regression)

Prédiction des ventes

(feature categorique et feature numérique)

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
