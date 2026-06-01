import math
def distance(a, b):
    total = 0
    for i in range(len(a)):
        total += (a[i] - b[i]) ** 2
    return math.sqrt(total)

def predict(X_train, y_train, test_point, k):
    dist_list = []
    for i in range(len(X_train)):
        d = distance(X_train[i], test_point)
        dist_list.append([d, y_train[i]])
    dist_list.sort()
    count0 = 0
    count1 = 0
    k = min(k, len(dist_list))

    for i in range(k):
        if dist_list[i][1] == 0:
            count0 += 1
        else:
            count1 += 1
    if count0 > count1:
        return 0
    else:
        return 1

def get_accuracy(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / len(actual)

def cross_validation(X, y, k, folds):
    size = len(X) // folds
    accuracies = []

    for i in range(folds):
        start = i * size
        end = start + size

        X_test = X[start:end]
        y_test = y[start:end]
        X_train = X[:start] + X[end:]
        y_train = y[:start] + y[end:]

        predictions = []
        for point in X_test:
            pred = predict(X_train, y_train, point, k)
            predictions.append(pred)

        acc = get_accuracy(y_test, predictions)
        accuracies.append(acc)
    return sum(accuracies) / len(accuracies)

X = [
    [1, 2], [2, 3], [3, 3],
    [6, 7], [7, 8], [8, 8]
]

y = [0, 0, 0, 1, 1, 1]

for k in [1, 3, 5]:
    result = cross_validation(X, y, k, 3)
    print("K =", k, "Accuracy =", result)