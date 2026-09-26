import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create dataset
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy',
                'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast',
                'Overcast', 'Rainy'],

    'Temp': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool',
             'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild',
             'Hot', 'Mild'],

    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal',
                 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High',
                 'Normal', 'High'],

    'Windy': [False, True, False, False, False, True,
              True, False, False, False, True, True,
              False, True],

    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No',
             'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes',
             'Yes', 'No']
}

df = pd.DataFrame(data)

# Convert categorical data into numbers
encoder = LabelEncoder()

df['Outlook'] = encoder.fit_transform(df['Outlook'])
df['Temp'] = encoder.fit_transform(df['Temp'])
df['Humidity'] = encoder.fit_transform(df['Humidity'])
df['Play'] = encoder.fit_transform(df['Play'])

# Input and output
X = df[['Outlook', 'Temp', 'Humidity', 'Windy']]
y = df['Play']

# Randomly split 10 training and 4 testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=10, test_size=4, random_state=42
)

# Test different tree parameters
parameters = [1, 2, 3, 4, 5]

for depth in parameters:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print("Max Depth =", depth)
    print("Accuracy =", accuracy)
    print()