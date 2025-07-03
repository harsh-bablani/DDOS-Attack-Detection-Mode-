from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from preprocessing import preprocess_data


def train_logistic_regression(X_train, X_test, y_train, y_test):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    return accuracy, cm


def train_mlp(X_train, X_test, y_train, y_test):
    model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    return accuracy, cm


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = preprocess_data(r'C:\Users\91800\Desktop\MainDS\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv')

    log_reg_accuracy, log_reg_cm = train_logistic_regression(X_train, X_test, y_train, y_test)
    print("Logistic Regression Accuracy:", log_reg_accuracy)
    print("Confusion Matrix (Logistic Regression):\n", log_reg_cm)

    mlp_accuracy, mlp_cm = train_mlp(X_train, X_test, y_train, y_test)
    print("MLP Accuracy:", mlp_accuracy)
    print("Confusion Matrix (MLP):\n", mlp_cm)
