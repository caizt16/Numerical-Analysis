# coding=utf-8

import numpy as np
from sympy import Symbol, expand
from scipy.optimize import fsolve
from numpy.polynomial import polynomial as P

# x_{k+1} = x_{k} - \lambda_{i} * f(x_{k}) / f'(x_{k})
class Damped_Newton(object):
    def __init__(self, coef, x, Epsilon, damped=True):
        super(Damped_Newton, self).__init__()
        self.x_pre = 0
        self.x = x

        self.function = P.Polynomial(coef)
        self.dfunction = self.function.deriv()

        self.Epsilon = Epsilon
        self.damped = damped

        self.cnt = 0
        self.string = expand(self.function(Symbol('x')))

        print('Solving %s ...' % self.string)

    def solve(self):
        while abs(self.function(self.x)) > self.Epsilon and abs(self.x - self.x_pre) > self.Epsilon:
            self.cnt += 1

            s = self.function(self.x) / self.dfunction(self.x)
            self.x_pre = self.x

            Lambda = 1.0
            while abs(self.function(self.x)) - abs(self.function(self.x_pre)) > -self.Epsilon:
                self.x = self.x_pre - Lambda * s

                if not self.damped:
                    self.x = self.x_pre - s
                    break

                # (2) 逐次折半
                Lambda /= 2

            # (3) 打印每个迭代步的最终\lambda值及近似解
            print ('iteration: %3d, lambda: %.3f, x: %.7f' % (self.cnt, Lambda, self.x))

        print('approx solution for %s is %.7f\n' % (self.string, self.x))
        return self.x


print('>>> USING DAMPED NEWTON METHOD')
solver = Damped_Newton(coef=(-1, -1, 0, 1), x=0.6,  Epsilon=1e-10)
solver.solve()

solver = Damped_Newton(coef=(0, 5, 0, -1), x=1.35, Epsilon=1e-10)
solver.solve()

print('>>> USING NORMAL NEWTON METHOD')
solver = Damped_Newton(coef=(-1, -1, 0, 1), x=0.6, Epsilon=1e-10, damped=False)
solver.solve()

solver = Damped_Newton(coef=(0, 5, 0, -1), x=1.35, Epsilon=1e-10, damped=False)
solver.solve()

print('>>> USING FZERO METHOD')
print fsolve(P.Polynomial((-1, -1, 0, 1)), 0.6)
print fsolve(P.Polynomial((0, 5, 0, -1)), 1.35)
