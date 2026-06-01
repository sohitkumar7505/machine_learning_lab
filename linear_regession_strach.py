from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv(
    "/Users/sohitkumar/Desktop/sohit/ML_LAB/to_upload/advertising.csv"
)


print(data.head())
print(data.info())


x = data['TV']
y = data['Sales']


plt.figure(figsize=(8, 5))
plt.scatter(x, y)
plt.xlabel('TV Advertising Budget')
plt.ylabel('Sales')
plt.title('TV Advertising Budget vs Sales')
plt.show()


def calculate_average(values):
    return sum(values) / len(values)

avg_x = calculate_average(x)
avg_y = calculate_average(y)


numerator = 0
denominator = 0

for i in range(len(x)):
    numerator += (x.iloc[i] - avg_x) * (y.iloc[i] - avg_y)
    denominator += (x.iloc[i] - avg_x) ** 2

m = numerator / denominator

b = avg_y - m * avg_x

print("Slope (m):", m)
print("Intercept (b):", b)
def predict(tv_budget):
    return m * tv_budget + b

print("Prediction for TV advertising budget of 150:",
      predict(150))
y_pred = predict(x)

plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x, y_pred, color='red', label='Regression Line')
plt.xlabel('TV Advertising Budget')
plt.ylabel('Sales')
plt.title('Linear Regression from Scratch')
plt.legend()
plt.show()