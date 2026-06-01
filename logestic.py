import numpy as np

X = np.array([[2],[4],[6],[8]])
y = np.array([0,0,1,1])

w = 0
b = 0
lr = 0.01
epochs = 1000

def sigmoid(z):
    return 1/(1+np.exp(-z))

for i in range(epochs):
    
    z = w*X + b
    y_pred = sigmoid(z)
    
    dw = (1/len(X)) * np.sum((y_pred - y) * X)
    db = (1/len(X)) * np.sum(y_pred - y)
    
    w = w - lr*dw
    b = b - lr*db

print("w:", w, "b:", b)