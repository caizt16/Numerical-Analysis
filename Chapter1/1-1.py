# coding=utf-8
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 指定默认字体
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['font.family']='sans-serif'
# 用来正常显示负号
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['text.usetex']=False
plt.rcParams['mathtext.fontset']='cm'

# 计算f(x) = sinx, 在x = 1点的导数值时的误差
truncation_error = lambda h: np.sin(1+h) * h / 2.
rounding_error = lambda h: 1e-16 * 2. / h
real_error = lambda h: np.abs(1. * (np.sin(1+h) - np.sin(1)) / h - np.cos(1))

# 绘制步长h-误差的对数关系图
plt.title(u"不同步长取值对应的差商近似导数的误差")
plt.xlabel(u"步长h")
plt.ylabel(u"误差")

x = np.logspace(-16, 0, num=100)
t = truncation_error(x)
r = rounding_error(x)
y = np.abs(t + r)
plt.ylim(1e-17, 10)
plt.loglog(x, t, linestyle="--", label=u'截断误差')
plt.loglog(x, r, linestyle="--", label=u'舍入误差')
plt.loglog(x, y, linestyle="--", label=u'总误差限')
plt.loglog(x, real_error(x), label=u'实际总误差')
plt.legend(loc=0, ncol=2)
plt.show()
