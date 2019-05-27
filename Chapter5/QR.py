import numpy as np

class QR(object):
    def __init__(self, A):
        super(QR, self).__init__()
        self.A = A
        self.w, self.h = A.shape

    def checkU(self):
        check = False
        for i in range(2, self.h):
            for j in range(0, i-1):
                if abs(self.A[i,j]) > 1e-9:
                    return False
        for i in range(1, self.h):
            if abs(self.A[i,i-1]) > 1e-9:
                if check:
                    return False
                else:
                    check = True
        return True

    def two_norm(self, vector):
        return np.sqrt(np.sum(np.square(vector)))

    def solve(self):
        while not self.checkU():
            Q = np.identity(self.h)
            for i in range(self.w):
                if self.A[i,i] < 0:
                    s = - self.two_norm(self.A[i:,i])
                if self.A[i,i] > 0:
                    s = self.two_norm(self.A[i:,i])

                v = np.zeros((self.h, 1), dtype=np.float64)
                v[i:,0] = self.A[i:,i]
                v[i,0] += s

                w = v / self.two_norm(v)
                H = np.identity(self.h) - 2 * np.dot(w, w.T)
                self.A = np.dot(H, self.A)
                Q = np.dot(Q, H)

            self.A = np.dot(self.A, Q)
        return self.A


# qr = QR(np.array([[2.9766, 0.3945, 0.4198, 1.1159], [0.3945, 2.7328, -0.3097, 0.1129], [0.4198, -0.3097, 2.5675, 0.6079], [1.1159, 0.1129, 0.6079, 1.7231]]))
qr = QR(np.array([[0.5, 0.5, 0.5, 0.5], [0.5, 0.5, -0.5, -0.5], [0.5, -0.5, 0.5, -0.5], [0.5, -0.5, -0.5, 0.5]]))
print qr.solve()
