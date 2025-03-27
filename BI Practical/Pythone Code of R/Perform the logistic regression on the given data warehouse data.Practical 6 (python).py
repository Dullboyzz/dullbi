import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load iris dataset
from sklearn import datasets
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['Species'] = iris.target

# Keep only first 100 rows (binary classification)
df = df.iloc[:100]

# Encode Species column (0 and 1)
le = LabelEncoder()
df['Species'] = le.fit_transform(df['Species'])

# Split data into training and test sets
np.random.seed(100)
train, test = train_test_split(df, train_size=0.8, random_state=100)

# Logistic Regression Model
X_train = train[['sepal length (cm)']]
y_train = train['Species']
X_test = test[['sepal length (cm)']]
y_test = test['Species']

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# Predict values
predicted_val = logreg.predict_proba(X_test)[:, 1]

# Create prediction DataFrame
prediction = pd.DataFrame({
    'Sepal.Length': X_test['sepal length (cm)'],
    'Species': y_test,
    'Predicted': predicted_val
})

# Plot predictions
plt.figure(figsize=(8, 6))
sns.scatterplot(x=prediction['Sepal.Length'], y=np.round(prediction['Predicted']), 
                hue=prediction['Species'], palette='viridis', s=100)
plt.xlabel("Sepal Length")
plt.ylabel("Prediction using Logistic Regression")
plt.title("Logistic Regression on Iris Data")
plt.legend(title='Species')
plt.grid()

# Save plot
plt.savefig("logistic_regression_iris.png")
plt.show()
