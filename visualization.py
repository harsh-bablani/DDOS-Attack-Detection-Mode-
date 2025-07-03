import matplotlib.pyplot as plt


def plot_accuracy(accuracy_log_reg, accuracy_mlp):
    models = ['Logistic Regression', 'MLP']
    accuracies = [accuracy_log_reg, accuracy_mlp]

    plt.bar(models, accuracies, color=['blue', 'green'])
    plt.ylabel('Accuracy')
    plt.title('Model Accuracy Comparison')
    plt.show()


if __name__ == "__main__":

    accuracy_log_reg = 0.95
    accuracy_mlp = 0.98
    plot_accuracy(accuracy_log_reg, accuracy_mlp)
