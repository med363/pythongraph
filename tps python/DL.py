import numpy as np


def sigmoid(x):
    return 1 / (1 +np.exp(-x))

def initialisation(X):
    W=np.random.randn(X.shape[1], 1)
    b = np.random.randn(1)
    return (W, b)


def forward_propagation(X,W,b):
    z =X.dot(w)+b
    A = sigmoid(z)
    return A

def log_loss(y,A):
    return 1/len(y) * np.sum(-y *np.log(A) - (1 - y) * np.log(1 - A))

def gradients(X,A,y):
    dw = 1/len(y) * np.dot(X.T,A -y)
    db = 1/len(y) * np.sum(A -y)
    return (dw, db)

def optimisation(X, W, b,A,y,learning_rate):
    dw,db = gradients(X,A,y)
    w = w - learning_rate * db
    b= b - learning_rate * db
    return(W,b)

def predict(X,W,b):
    A = forward_propagation(X,W,b)
    return A >=0.5
