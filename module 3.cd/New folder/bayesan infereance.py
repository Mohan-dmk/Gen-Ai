# spam_detector_bayes.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Step 1: Load dataset (from a public URL)
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep='\t', names=['label', 'message'])

# Step 2: Convert labels to numbers (spam = 1, ham = 0)
df['label_num'] = df.label.map({'ham': 0, 'spam': 1})

# Step 3: Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label_num'], test_size=0.2, random_state=42)

# Step 4: Convert text messages into word counts
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# Step 5: Train Naive Bayes model
model = MultinomialNB()
model.fit(X_train_counts, y_train)

# Step 6: Check accuracy on test data
y_pred = model.predict(X_test_counts)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Step 7: Predict a new message
user_input = input("Enter your message: ")
new_message = [user_input]
new_message_counts = vectorizer.transform(new_message)
prediction = model.predict(new_message_counts)
probabilities = model.predict_proba(new_message_counts)

# Step 8: Show prediction and probabilities
label = "Spam" if prediction[0] == 1 else "Not Spam"
print(f"Prediction: {label}")
print(f"Probability it's Spam: {probabilities[0][1]:.2f}")
print(f"Probability it's Not Spam: {probabilities[0][0]:.2f}")
