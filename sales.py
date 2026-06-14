from sklearn.linear_model import LinearRegression

# Advertising budget
X = [[10], [20], [30], [40], [50]]

# Sales
y = [100, 200, 300, 400, 500]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[60]])

print("Predicted Sales:", prediction[0])