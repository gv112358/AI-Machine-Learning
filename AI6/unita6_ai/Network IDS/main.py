# Importing necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.naive_bayes import BernoulliNB
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import sys

# Ignoring warnings
import warnings
warnings.filterwarnings('ignore')

# Setting display options for better interaction
pd.set_option('display.max_columns', None)
sns.set(style="whitegrid")
plt.style.use('seaborn-darkgrid')
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

# Loading training and testing data
train = pd.read_csv("data/Train_data.csv")
test = pd.read_csv("data/Test_data.csv")

# Displaying a snippet of the training data
print("Training Data:")
print(train.head())

# Displaying a snippet of the testing data
print("\nTesting Data:")
print(test.head())

# Checking and dropping redundant column 'num_outbound_cmds'
train.drop(['num_outbound_cmds'], axis=1, inplace=True)
test.drop(['num_outbound_cmds'], axis=1, inplace=True)

# Analyzing attack class distribution in the training data
plt.figure(figsize=(8, 6))
sns.countplot(x='class', data=train, palette='Set2')  # Using a different color palette
plt.title('Distribution of Attack Classes in Training Data')
plt.xlabel('Attack Class')
plt.ylabel('Count')
plt.show()

# Feature Scaling: Scaling numerical attributes to have zero mean and unit variance
scaler = StandardScaler()
num_cols = train.select_dtypes(include=['float64', 'int64']).columns
sc_train = scaler.fit_transform(train.select_dtypes(include=['float64', 'int64']))
sc_test = scaler.fit_transform(test.select_dtypes(include=['float64', 'int64']))
sc_traindf = pd.DataFrame(sc_train, columns=num_cols)
sc_testdf = pd.DataFrame(sc_test, columns=num_cols)

# Label Encoding: Encoding categorical attributes
encoder = LabelEncoder()
cat_cols_train = train.select_dtypes(include=['object']).columns
cat_cols_test = test.select_dtypes(include=['object']).columns
train_encoded = train[cat_cols_train].apply(encoder.fit_transform)
test_encoded = test[cat_cols_test].apply(encoder.fit_transform)

# Combining numerical and encoded categorical features
train_x = pd.concat([sc_traindf, train_encoded], axis=1)
test_df = pd.concat([sc_testdf, test_encoded], axis=1)

# Initializing and fitting a RandomForestClassifier for feature importance
rfc = RandomForestClassifier()
rfc.fit(train_x, train['class'])
feature_importance = pd.Series(rfc.feature_importances_, index=train_x.columns).sort_values(ascending=False)

# Plotting feature importances
plt.figure(figsize=(12, 6))
sns.barplot(x=feature_importance.index, y=feature_importance, palette='Set2')  # Using a different color palette
plt.title('Feature Importances')
plt.xlabel('Feature')
plt.ylabel('Importance')
plt.xticks(rotation=45, ha='right')
plt.show()

# Selecting top 15 features using Recursive Feature Elimination (RFE)
rfc = RandomForestClassifier()
rfe = RFE(rfc, n_features_to_select=15)
rfe = rfe.fit(train_x, train['class'])
selected_features = train_x.columns[rfe.support_]

# Splitting the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(train_x, train['class'], train_size=0.70, random_state=2)

# Initializing various classifiers
KNN_Classifier = KNeighborsClassifier(n_jobs=-1)
LGR_Classifier = LogisticRegression(n_jobs=-1, random_state=0, max_iter=1000)  # Increased max_iter
BNB_Classifier = BernoulliNB()  # Corrected: Removed '()' after BernoulliNB
DTC_Classifier = tree.DecisionTreeClassifier(criterion='entropy', random_state=0)

# Fitting BernoulliNB Classifier
BNB_Classifier.fit(X_train, Y_train)

# Training and evaluating multiple classifiers
models = [
    ('Naive Baye Classifier', BNB_Classifier),
    ('Decision Tree Classifier', DTC_Classifier),
    ('KNeighbors Classifier', KNN_Classifier),
    ('Logistic Regression', LGR_Classifier)
]

for model_name, model in models:
    # Ensure the model is fitted before making predictions or evaluating accuracy
    if model_name != 'Naive Baye Classifier':
        model.fit(X_train, Y_train)

    scores = cross_val_score(model, X_train, Y_train, cv=10)
    accuracy = metrics.accuracy_score(Y_train, model.predict(X_train))
    confusion_matrix = metrics.confusion_matrix(Y_train, model.predict(X_train))
    classification = metrics.classification_report(Y_train, model.predict(X_train))

    # Model Evaluation
    print('\n============================== {} Model Evaluation =============================='.format(model_name))
    print('\nCross Validation Mean Score:\n', scores.mean())
    print('\nModel Accuracy:\n', accuracy)
    print('\nConfusion Matrix:\n', confusion_matrix)
    print('\nClassification Report:\n', classification)

# Testing the models on the test set
for model_name, model in models:
    accuracy = metrics.accuracy_score(Y_test, model.predict(X_test))
    confusion_matrix = metrics.confusion_matrix(Y_test, model.predict(X_test))
    classification = metrics.classification_report(Y_test, model.predict(X_test))

    # Model Test Results
    print('\n============================== {} Model Test Results =============================='.format(model_name))
    print('\nModel Accuracy:\n', accuracy)
    print('\nConfusion Matrix:\n', confusion_matrix)
    print('\nClassification Report:\n', classification)

# Making predictions on the test data
# Ensure the feature names in the test dataset match the features used during training
test_df = test_df[X_train.columns]
pred_knn = KNN_Classifier.predict(test_df)
pred_NB = BNB_Classifier.predict(test_df)
pred_log = LGR_Classifier.predict(test_df)
pred_dt = DTC_Classifier.predict(test_df)

# Additional analysis or reporting on final predictions
# Combine predictions into a DataFrame for easier analysis
predictions_df = pd.DataFrame({
    'KNN_Predictions': pred_knn,
    'NB_Predictions': pred_NB,
    'Logistic_Predictions': pred_log,
    'DecisionTree_Predictions': pred_dt
})

# Visualizing the distribution of predictions
plt.figure(figsize=(12, 8))
sns.countplot(data=predictions_df.melt(), x='value', hue='variable', palette='viridis', alpha=0.8)
plt.title('Distribution of Predictions by Different Models')
plt.xlabel('Predicted Class')
plt.ylabel('Count')
plt.legend(title='Models', loc='upper right')
plt.show()

# Comparing the predictions of different models
plt.figure(figsize=(10, 6))
sns.heatmap(predictions_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation of Predictions Between Different Models')
plt.show()

# Generating insights or additional analysis based on the predictions
# Example: Counting instances where all models agree on predictions
unanimous_predictions = predictions_df.apply(lambda x: len(set(x)) == 1, axis=1)
unanimous_count = unanimous_predictions.sum()

print(f"\nInstances where all models agree on predictions: {unanimous_count}")
