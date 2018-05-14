
# Import Grid Search and MLP model from sklearn.
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier

# Creating a MLP model
model = MLPClassifier() # Creating a MLP to optimise

# Setting up a range of hyperparameters for the grid search
param_grid = [{'activation':['identity','relu']},
              {'solver':['lbfgs','sgd','adam']},
              {'hidden_layer_sizes':[(5),(5,5),(10,10)]}]

# Setting up the grid search with model, parameter and scoring method
gs = GridSearchCV(estimator=model,
                  param_grid=param_grid,
                  scoring='accuracy')

# Running the grid search model and saving the best model
gs = gs.fit(X_train, y_train)

# Print the best score and the best parameters
print(gs.best_score_)
print(gs.best_params_)