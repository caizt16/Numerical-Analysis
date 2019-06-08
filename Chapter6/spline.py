import numpy as np
import matplotlib.pyplot as plt

def S(query):
    global x, y, n, h, A, d, M
    i = -1
    for ii in range(n-1):
        if query >= x[ii] and query <= x[ii+1]:
            i = ii
            break
    if i == -1:
        return -1

    return M[i] * np.power(x[i+1] - query, 3) / (6.0 * h[i]) \
    + M[i+1] * np.power(query - x[i], 3) / (6.0 * h[i]) \
    + (y[i] - M[i] * h[i] * h[i] / 6.0) * ((x[i+1] - query) / h[i]) \
    + (y[i+1] - M[i+1] * h[i] * h[i] / 6.0) * ((query - x[i]) / h[i])

def S1(query):
    global x, y, n, h, A, d, M
    i = -1
    for ii in range(n-1):
        if query >= x[ii] and query <= x[ii+1]:
            i = ii
            break
    if i == -1:
        return -1

    return -1.0 * M[i] * np.power(x[i+1] - query, 2) / (2.0 * h[i]) \
    + 1.0 * M[i+1] * np.power(query - x[i], 2) / (2.0 * h[i]) \
    + 1.0 * (y[i+1] - y[i]) / h[i] \
    - 1.0 * h[i] * (M[i+1] - M[i]) / 6.0

def S2(query):
    global x, y, n, h, A, d, M
    i = -1
    for ii in range(n-1):
        if query >= x[ii] and query <= x[ii+1]:
            i = ii
            break
    if i == -1:
        return -1

    return 1.0 * M[i] * (x[i+1] - query) / h[i] \
    + 1.0 * M[i+1] * (query - x[i]) / h[i]

x = np.array([0.520, 3.1, 8.0, 17.95, 28.65, 39.62, 50.65, 78, 104.6, 156.6, 208.6, 260.7, 312.5, 364.4, 416.3, 468, 494, 507, 520])
y = np.array([5.288, 9.4, 13.84, 20.20, 24.90, 28.44, 31.10, 35, 36.9, 36.6, 34.6, 31.0, 26.34, 20.9, 14.8, 7.8, 3.7, 1.5, 0.2])
dy0, dyn = 1.86548, -0.046115

n = x.shape[0]
h = np.array([x[i+1] - x[i] for i in range(n-1)])
A = np.zeros((n, n))
for i in range(n):
    A[i, i] = 2
    if i + 1 < n:
        A[i, i + 1] = 1 if i == 0 else (1.0 * h[i] / (h[i-1] + h[i]))
    if i - 1 >= 0:
        A[i, i - 1] = 1 if i == n-1 else (1.0 * h[i-1] / (h[i-1] + h[i]))

d = np.zeros(x.shape)
d[0] = 6.0 / h[0] * (1.0 * (y[1] - y[0]) / h[0] - dy0)
d[n-1] = 6.0 / h[n-2] * (dyn - 1.0 * (y[n-1] - y[n-2]) / h[n-2])
for i in range(1, n-1):
    d[i] = 6.0 * (1.0 * y[i-1] / (h[i-1] * (h[i-1] + h[i])) + 1.0 * y[i+1] / (h[i] * (h[i-1] + h[i])) - 1.0 * y[i] / (h[i-1] * h[i]))

M = np.linalg.solve(A, d)

def get_ans(x):
    print 'f(x):', S(x)
    print 'f\'(x):', S1(x)
    print 'f\'\'(x):', S2(x)

get_ans(2)
get_ans(30)
get_ans(130)
get_ans(350)
get_ans(515)

plt.plot(x, y)
rx = np.arange(1, 500, 5)
ry = []
ryy = []
ryyy = []
for xx in rx:
    ry.append(S(xx))
    ryy.append(S1(xx))
    ryyy.append(S2(xx))
plt.plot(rx, ry)
#plt.plot(rx, ryy)
#plt.plot(rx, ryyy)
plt.show()
#print ryy
#print ryyy
