
#求函数f(x)的极限
#lim(x->∞)(2*x**(5/3) - x**(1/3) + 7)/(x**(8/5) + 3*x + x**(1/2))
#=lim(x->∞)(2 - x**(-4/3) + 7*x**(-5/3))/(x**(-1/15) + 3*x**(-2/3) + x**(-7/6))
#从这里看出极限是无穷
def f(x):
    return (2*x**(5.0/3.0) - x**(1.0/3.0) + 7)/(x**(8.0/5.0) + 3*x + x**(1.0/2.0))

x = linspace(1, 100, 100)
y = f(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')
