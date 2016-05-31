#设f(x) = (x + 6)/(x**2 + 4*x - 12)
#
#(a)对点x = -5.9, -5.99, -5.999等处的f值列表, 估算lim(x->-6)f(x), 如果能代之以f在x = -6.1, -6.01, -6.001#处的值, 又能估算得到什么

#(b)用f(x) 在x0=-6附近的图来说明

#(c)代数地求lim(x->-6)f(x)
#f(x) = (x + 6) / (x + 6)*(x - 2)
#     = 1 / (x - 2) x != -6
#                                           lim(x->-6)f(x) = -1/8

def f(x):
    return (x + 6) / (x**2 + 4*x - 12)

fl1 = f(-6.1)
fl2 = f(-6.01)
fl3 = f(-6.001)
fl4 = f(-6.0001)
fl5 = f(-6.00001)

fr1 = f(-5.9)
fr2 = f(-5.99)
fr3 = f(-5.999)
fr4 = f(-5.9999)
fr5 = f(-5.99999)

print 'fl(%f, %f, %f, %f, %f) fr(%f, %f, %f, %f, %f)' % (fl1, fl2, fl3, fl4, fl5, fr1, fr2, fr3, fr4, fr5)


x1 = linspace(-8, -6.0000001, 100)
y1 = f(x1)

x2 = linspace(-5.9999999, -4, 100)
y2 = f(x2)


xlabel('x')
ylabel('y')
plot(x1, y1, 'r-', x2, y2, 'g-')
