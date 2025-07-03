import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np


def preprocess_data(file_path):
    df = pd.read_csv(file_path)

    df.columns = df.columns.str.strip()

    print("Columns in dataset:", df.columns)

    df = df.dropna()

    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)

    X = df.drop(columns=['Label'])

    y = df['Label']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    file_path = r'C:\Users\91800\Desktop\MainDS\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv'
    X_train, X_test, y_train, y_test = preprocess_data(file_path)
    print("Data preprocessing completed.")
