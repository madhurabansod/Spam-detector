import pandas as pd 
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# 1. Read spam.csv using pandas
# Note: Many spam datasets use 'latin-1' encoding
df = pd.read_csv('spam.csv', encoding='latin-1')

# 2. Preprocess & Convert labels
# Standard spam.csv has labels in 'v1' and text in 'v2'
df = df[['v1', 'v2']]  # Keep only necessary columns
df.columns = ['label', 'message']  # Rename for clarity

# Convert labels: ham -> 0, spam -> 1
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# 3. Split data into Training and Testing sets
X = df['message']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Use TfidfVectorizer to convert text to numbers
vectorizer = TfidfVectorizer(stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# 5. Initialize and Train the MultinomialNB model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# 6. Print Accuracy
y_pred = model.predict(X_test_tfidf)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# 7. Save model.pkl and vectorizer.pkl
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('vectorizer.pkl', 'wb') as vec_file:
    pickle.dump(vectorizer, vec_file)

print("Model and Vectorizer saved successfully!") 
