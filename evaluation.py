import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from train import train_logistic_regression, train_mlp
from preprocessing import preprocess_data

def plot_confusion_matrix(cm, title):
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Normal', 'Attack'], yticklabels=['Normal', 'Attack'])
    plt.title(title)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = preprocess_data(r'C:\Users\91800\Desktop\MainDS\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv')

    log_reg_accuracy, log_reg_cm = train_logistic_regression(X_train, X_test, y_train, y_test)
    print("Logistic Regression Accuracy:", log_reg_accuracy)
    plot_confusion_matrix(log_reg_cm, "Logistic Regression Confusion Matrix")

    mlp_accuracy, mlp_cm = train_mlp(X_train, X_test, y_train, y_test)
    print("MLP Accuracy:", mlp_accuracy)
    plot_confusion_matrix(mlp_cm, "MLP Confusion Matrix")
