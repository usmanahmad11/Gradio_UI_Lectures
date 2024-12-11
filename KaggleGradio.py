import gradio as gr
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load Titanic dataset (already available in Kaggle's Titanic competition datasets)
data = pd.read_csv("/kaggle/input/titanic/train.csv")

# Preprocessing
data = data[["Pclass", "Sex", "Age", "Survived"]].dropna()
data["Sex"] = data["Sex"].map({"male": 0, "female": 1})

# Train a model
X = data[["Pclass", "Sex", "Age"]]
y = data["Survived"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Prediction function
def predict_survival(pclass, sex, age):
    sex = 0 if sex.lower() == "male" else 1
    prediction = model.predict([[pclass, sex, age]])[0]
    return "Survived" if prediction == 1 else "Did not survive"

# Gradio Interface
interface = gr.Interface(
    fn=predict_survival,
    inputs=[
        gr.Dropdown(["1", "2", "3"], label="Passenger Class"),
        gr.Dropdown(["Male", "Female"], label="Sex"),
        gr.Slider(0, 80, label="Age"),
    ],
    outputs="text",
    title="Titanic Survival Predictor",
    description="Predict if a Titanic passenger would survive based on their class, sex, and age.",
)

# Launch the interface with 'share=True' for Kaggle
interface.launch(share=True)
