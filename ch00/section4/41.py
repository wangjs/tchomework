
#某种放射性物质的半衰期是12个小时， 一开始这种物质有8克
#(a)把该物质的剩余量表示为时间t的函数:f(t) = 8 * 0.5**(t/12)
#(b)何时剩余量只剩下一克
#求反函数：
#y = 8 * 0.5**(t/12)
#y/8 = 0.5**(t/12)
#log0.5(y/8) = t/12
#12*log0.5(y/8) = t
#g(x) = 12*ln(x/8)/ln(0.5)

def g(x):
    return 12*log(x/8)/log(0.5)


x = linspace(8, 1, 100)
y = g(x)


xlabel('x')
ylabel('y')
plot(x, y, 'r-')