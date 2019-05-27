import numpy as np

class Iterative_Solver(object):
    def __init__(self, epsilon, a, n):
        self.epsilon = epsilon
        self.a = a
        self.n = n + 1
        self.h = 1.0 / n

        self.A = np.zeros((self.n,self.n))
        for i in range(self.n):
            self.A[i, i] = -(2*self.epsilon + self.h)
            if i-1 >= 0:
                self.A[i, i-1] = self.epsilon
            if i+1 < self.n:
                self.A[i, i+1] = self.epsilon + self.h
        #self.A[0,0] = -(self.epsilon + self.h)
        #self.A[-1,-1] = -self.epsilon

        self.b = np.zeros((self.n,1))
        self.b[:,0] = self.a * self.h * self.h

        self.error = 1e-6

    def Jacobian(self):
        return self.SOR(jacobian=True)

    def Gauss_Seidel(self):
        return self.SOR()

    def SOR(self, omega=1.0, jacobian=False):
        cnt = 0
        self.x = np.zeros((self.n,1))
        self.x[0,0] = 0.0
        self.x[-1,0] = 1.0
        pre_x = np.ones((self.n,1))

        #while np.max(np.abs(self.b - np.dot(self.A, self.x))) > self.error:
        #while np.max(np.abs(self.x - pre_x)) > self.error:
        while np.sqrt(np.sum(np.square(self.x - pre_x))) > self.error:
            cnt += 1
            pre_x = np.copy(self.x)

            if jacobian:
                y = np.copy(self.x)
            else:
                y = self.x

            for i in range(1, self.n - 1):
                self.x[i,0] = (1-omega) * self.x[i,0] + omega * (self.b[i,0] - np.dot(self.A[i,:], y)[0] + self.A[i,i]*y[i,0]) / self.A[i,i]

        return cnt, self.x[:-1,0]

    def Direct(self):
        self.x = np.arange(0, 1, 1.0 / (self.n - 1)).reshape((self.n-1, 1))
        return ((1 - self.a) * (1 - np.exp(-self.x / self.epsilon)) / (1 - np.exp(-1 / self.epsilon)) + self.a * self.x)

class Eval(object):
    def __init__(self):
        self.j = 0
        self.gs = 0
        self.sor = 0
        self.true = 0

    def compare(self):
        print 'jacobian error: %.7f' % np.max(np.abs(np.subtract(self.j, self.true)))
        print 'gs error: %.7f' % np.max(np.abs(np.subtract(self.gs, self.true)))
        print 'sor error: %.7f' % np.max(np.abs(np.subtract(self.sor, self.true)))

solver = Iterative_Solver(0.001, 0.5, 100)
evaler = Eval()
evaler.j = solver.Jacobian()[1]
#print evaler.j
evaler.gs = solver.Gauss_Seidel()[1]
evaler.sor = solver.SOR(omega=1.1)[1]
evaler.sor = solver.SOR(omega=1.2)[1]
#print evaler.gs
evaler.true = solver.Direct()[1]
#print evaler.true
#print solver.b, np.dot(solver.A, evaler.true)
evaler.compare()

