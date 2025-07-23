# Spam Email Detection using Scikit-learn

# 1. Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 2. Load dataset
# Using a popular spam dataset: 'SMSSpamCollection' from UCI repository
import urllib.request
url = 'https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv'
df = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])

# 3. Preview data
print(df.head())

# 4. Convert labels to binary
df['label_num'] = df.label.map({'ham': 0, 'spam': 1})

# 5. Text preprocessing (Vectorization)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['message'])  # Feature matrix
y = df['label_num']                          # Labels

# 6. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 7. Model training - Multinomial Naive Bayes
model = MultinomialNB()
model.fit(X_train, y_train)

# 8. Prediction
y_pred = model.predict(X_test)

# 9. Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 10. Optional - Visualize confusion matrix
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
