from flask import Flask, render_template, jsonify
from app import app
from plots import generate_confusion_matrix, generate_accuracy_plot
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd

@app.route('/')
def index():

    df = pd.read_csv(r'C:\Users\91800\Desktop\MainDS\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv')
    df = df.dropna()
    X = df.drop(columns=['Label'])
    y = df['Label']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

    log_reg = LogisticRegression()
    log_reg.fit(X_train, y_train)
    log_reg_pred = log_reg.predict(X_test)
    log_reg_accuracy = accuracy_score(y_test, log_reg_pred)

    mlp = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000)
    mlp.fit(X_train, y_train)
    mlp_pred = mlp.predict(X_test)
    mlp_accuracy = accuracy_score(y_test, mlp_pred)

    generate_confusion_matrix(y_test, log_reg_pred, 'Logistic Regression')
    generate_confusion_matrix(y_test, mlp_pred, 'MLP')

    generate_accuracy_plot(log_reg_accuracy, mlp_accuracy)

    return render_template('index.html',
                           log_reg_accuracy=log_reg_accuracy,
                           mlp_accuracy=mlp_accuracy)

if __name__ == "__main__":
    app.run(debug=True)
