
# Import machine learning model from sklearn
from sklearn.neural_network import MLPClassifier

# Create the model - Settings goes within the brackets
model = MLPClassifier(hidden_layer_sizes=(25,25), solver='lbfgs')

# Train the model
model.fit(X_train, y_train)

# Predict with the trained model
predictions = model.predict(X_test)