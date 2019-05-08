import numpy as np

class Hilbert(object):
    def __init__(self, n):
        super(Hilbert, self).__init__()
        self.n = n
        self.values = np.zeros((n, n))

        for i in range(n):
            for j in range(n):
                self.values[i,j] = 1.0 / (1+i+j)

    def getB(self):
        x = np.ones((self.n, 1))
        return np.dot(self.values, x)

class Cholesky(object):
    def __init__(self, A, b):
        super(Cholesky, self).__init__()
        self.A = A
        self.b = b
        self.y = np.zeros(b.shape)
        self.x = np.zeros(b.shape)
        self.n = self.A.shape[0]

    def factorize(self):
        for j in range(self.n):
            for k in range(j):
                self.A[j,j] -= np.square(self.A[j,k])

            self.A[j,j] = np.sqrt(self.A[j,j])

            for i in range(j+1, self.n):
                for k in range(j):
                    self.A[i,j] -= self.A[i,k] * self.A[j,k]
                self.A[i,j] /= self.A[j,j]

    def solveL(self):
        b = np.copy(self.b)
        for i in range(self.n):
            for j in range(i):
                b[i,0] -= self.y[j,0] * self.A[i,j]

            self.y[i,0] = b[i,0] / self.A[i,i]

    def solveLT(self):
        for i in range(self.n-1, -1, -1):
            for j in range(i+1, self.n):
                self.y[i,0] -= self.x[j,0] * self.A.T[i,j]

            self.x[i,0] = self.y[i,0] / self.A.T[i,i]


    def solve(self):
        self.factorize()
        self.solveL()
        self.solveLT()

    def get_r_residual(self):
        return np.max(self.b - np.dot(self.A, self.x))

    def get_delta_x_residual(self):
        return np.max(self.x - np.ones(self.x.shape))

def hc_solver(n, disturb=False):
    hilbert = Hilbert(n)
    H = hilbert.values
    b = hilbert.getB()

    if disturb:
        b += np.power(10.0, -6) * np.random.uniform(-1,1,b.shape)

    cholesky = Cholesky(H, b)
    cholesky.solve()

    print ('n = %2d' % n)
    print ('r-infinity is %.7f' % cholesky.get_r_residual())
    print ('delta x-infinity is %.7f\n' % cholesky.get_delta_x_residual())

hc_solver(10)
hc_solver(10, disturb=True)
hc_solver(8)
hc_solver(12)
