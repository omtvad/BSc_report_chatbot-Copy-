
# Import machine learning model from sklearn
from sklearn.cluster import KMeans

# Create the model - Settings goes within the brackets
model = KMeans(n_clusters=2, random_state=0)

# Train the model
model.fit(data)

# Predict with the trained model
predictions = model.predict(data)

# ------ Alternatively ------ #

# Train and predict
predictions = model.fit_predict(data)





