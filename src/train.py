from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

print("AI is studying the data...")

data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train,y_train)

os.makedirs("models", exist_ok=True)

joblib.dump(model,"models/model.pkl")

print("Success! The Model Brain is saved in the 'models' folder.")