from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Split data into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

# Different neural network architectures
architectures = [
    (5,),
    (10,),
    (10, 5),
    (20, 10)
]

# Different training functions
functions = ['relu', 'tanh', 'logistic']

# Train and test different models
for architecture in architectures:
    for function in functions:

        model = MLPClassifier(
            hidden_layer_sizes=architecture,
            activation=function,
            solver='adam',
            max_iter=2000,
            random_state=42
        )

        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)

        print("Architecture:", architecture)
        print("Training Function:", function)
        print("Accuracy:", accuracy)
        print()