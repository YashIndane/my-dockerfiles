# Random Forest Classification

import numpy as np
import pandas as pd
import joblib
import os
from subprocess import getstatusoutput as gso


#defining enviornment variables
ts = os.environ['TEST_SIZE']
rs = os.environ['RANDOM_STATE']
es = os.environ['TREES']
cri = os.environ['CRITERIA']
user_name = os.environ['GIT_USRN']
repo_name = os.environ['GIT_REPON']
name = os.environ['GNAME']
email = os.environ['GEMAIL']

FILE_PATH = '/ml_folder/train.csv'

while(not os.path.isfile(FILE_PATH)) : pass

# Importing the dataset
dataset = pd.read_csv(FILE_PATH)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = float(ts), random_state = int(rs))

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
joblib.dump(sc , '/ml_folder/scalar')

# Training the Random Forest Classification model on the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = int(es), criterion = cri , random_state = int(rs))
classifier.fit(X_train, y_train)
joblib.dump(classifier , '/ml_folder/model')

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(f'''confusion matrix
{cm}''')


#pushing code to repo
status = gso('mkdir /git-ws')
status = gso('git init /git-ws')
status = gso(f'cd /git-ws && git remote add origin https://github.com/{user_name}/{repo_name}.git')
print(status[1])
status = gso('mv /ml_folder/model /git-ws')
status = gso('mv /ml_folder/scalar /git-ws')
status = gso('cd /git-ws && git add .')
status = gso(f'cd /git-ws && git config user.name "{name}"')
status = gso(f'cd /git-ws && git config user.email "{email}"')
status = gso('cd /git-ws && git commit -m "committing model" .')
status = gso('cd /git-ws && git branch -M main')
status = gso('cd /git-ws && git push -u origin main')
print(status[1])






