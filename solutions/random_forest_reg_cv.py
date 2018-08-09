from sklearn.model_selection import GridSearchCV

param_grid = {'n_estimators': [300, 400, 500, 600],
              'max_leaf_nodes': [10, 20, 30, 40],
              }

clf = RandomForestRegressor(max_depth=9, 
                            min_samples_leaf=10)
rf_cv = GridSearchCV(clf, param_grid, n_jobs=4, cv=5).fit(X, y)

# best hyperparameter setting
rf_cv.best_params_