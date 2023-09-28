# Import necessary libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
# Sample dataset (replace with your actual dataset)
df = pd.read_csv("D:\SIH_Void_TYPHOONS\server\DataExcel.csv")
data = df.to_dict(orient='records')
# data = [
#     {"interests": "programming, problem-solving", "career": "Software Developer", "undergrad_course": "Computer Science", "postgrad_course": "Data Science"},
#     {"interests": "design, creativity", "career": "Graphic Designer", "undergrad_course": "Graphic Design", "postgrad_course": "Graphic Design"},
#     {"interests": "Finance, Economics", "career": "Financial Analyst", "undergrad_course": "Finance", "postgrad_course": "Economics"},
#     {"interests": "design, creativity", "career": "Graphic Designer", "undergrad_course": "Graphic Design", "postgrad_course": "Graphic Design"},
#     # Add more data points as needed
# ]

# Separate features (interests) and labels (careers) from the dataset
interests = [entry['interests'] for entry in data]
careers = [entry['career'] for entry in data]

# Vectorize the interests using TF-IDF (Term Frequency-Inverse Document Frequency)
tfidf_vectorizer = TfidfVectorizer()
X = tfidf_vectorizer.fit_transform(interests)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X, careers)


def recommend_career(user_interests):
    # Use the trained model to predict career recommendations
    X_user = tfidf_vectorizer.transform([user_interests])
    predicted_career = classifier.predict(X_user)
    
    # Find the corresponding undergraduate and postgraduate courses
    index = careers.index(predicted_career[0])
    undergrad_course = data[index]['undergrad_course'] if 'undergrad_course' in data[index] else "N/A"
    postgrad_course = data[index]['postgrad_course'] if 'postgrad_course' in data[index] else "N/A"
    
    return {
        "Recommended Career": predicted_career[0],
        "Undergraduate Course": undergrad_course,
        "Postgraduate Course": postgrad_course,
    }


# Example input from the user
user_interests = "programming, problem-solving"
recommendation = recommend_career(user_interests)
print("**********",end=" ")
print(f"Recommended Career: {recommendation['Recommended Career']}",end="")
print("*****************")
print("Courses:")
print(f"Undergraduate Course: {recommendation['Undergraduate Course']}")
print(f"Postgraduate Course: {recommendation['Postgraduate Course']}")
