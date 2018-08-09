
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_jobs=4, criterion='entropy')
rf.fit(X_train, y_train)

y_train_pred = rf.predict(X_train)

from sklearn.metrics import precision_score

precision_score(y_train, y_train_pred)
