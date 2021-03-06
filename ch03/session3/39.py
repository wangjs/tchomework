#求函数图形的拐点, 以及函数的局部极值
#一二阶导数和x轴交点和函数的图形有怎样的关系?
#导数的图形以怎样的另一种形式和函数的图形相关
#y = f(x) = 4/5*x**5 + 16*x**2 - 25
#y'= 0 的根为 x = -2, x = 0
#y''= 0 的根为x = -1.26

#首先看x = -2处, 应用局部极值的二阶导数检测法, 该点取得局部最大值
#再看x = 0处, 应用局部极值的二阶导数检测法该点取得局部最小值
#拐点, x = -1.26处, 凹性改变是拐点

#一阶导函数的根,是可能的局部极值点
#二阶导函数的根, 是可能的凹性改变的地方
#导数图形的增性, 决定了函数图形的凹性

def f(x):
    return 4.0/5.0*x**5 + 16*x**2 - 25

def fd(x):
    return 4*x**4 + 32*x

def fdd(x):
    return 16*x**3 + 32


plot([-3, 5.4], [0, 0], '-k')

x = linspace(-3, 3, 1000)
y = f(x)
yd= fd(x)
ydd=fdd(x)
plot(x, y, '-r', x, yd, '-g', x, ydd, '-b')
