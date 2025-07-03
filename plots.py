import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

def generate_confusion_matrix(y_true, y_pred, model_name):
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Normal', 'Attack'], yticklabels=['Normal', 'Attack'])
    plt.title(f'{model_name} Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.savefig(f'app/static/images/{model_name}_confusion_matrix.png')
    plt.close()

def generate_accuracy_plot(log_reg_accuracy, mlp_accuracy):
    models = ['Logistic Regression', 'MLP']
    accuracies = [log_reg_accuracy, mlp_accuracy]

    fig = px.bar(x=models, y=accuracies, labels={'x': 'Models', 'y': 'Accuracy'}, title="Model Accuracy Comparison")
    fig.write_html("app/static/images/accuracy_comparison.html")
