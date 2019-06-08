import numpy as np
import matplotlib.pyplot as plt

def poly(t, y):
    A = np.array([np.ones(t.shape), t, np.power(t, 2) ])
    x = np.linalg.solve(np.dot(A, A.T), np.dot(A, y.T))
    print 'error: %.5f' % two_norm(np.dot(A.T, x), y)
    return x, np.dot(A.T, x)

def exp(t, y):
    log_y = np.log(y)
    A = np.array([np.ones(t.shape), t])
    x = np.linalg.solve(np.dot(A, A.T), np.dot(A, log_y.T))
    print 'error: %.5f' % two_norm(np.exp(np.dot(A.T, x)), y)
    return x, np.exp(np.dot(A.T, x))

def two_norm(x, y):
    return np.sqrt(np.sum(np.square(np.subtract(x, y))))

t = np.arange(1, 8.5, 0.5)
y = np.array([33.40, 79.50, 122.65, 159.05, 189.15, 214.15, 238.65, 252.2, 267.55, 280.50, 296.65, 301.65, 310.40, 318.15, 325.15])

x, py = poly(t, y)
print(py)

x, ey = exp(t, y)
print(ey)

plt.plot(t, y)
plt.plot(t, py)
plt.plot(t, ey)
plt.show()
