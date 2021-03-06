#折纸
#8.5*11的矩形纸片放在平坦的面上, 通过折叠把一个角放在较长的对边上
#并保持纸片是光滑平坦的. 问题是使得折痕L的长度尽可能的小
#(a)证明L**2 = 2*x**3 / (2*x - 8.5)
#(b)怎样的x值使得L**2最小
#(c)L的最小值是什么

def Lsq(h):
    return 2*x**3 / (2*x - 8.5)

def Lsqd(h):
    return (8*x**3 - 51*x**2) / (4*x**2 - 34*x + 72.25)

def Lsqdd(h):
    return (32*x**4 - 544*x**3 + 3468*x**2 - 7369.5*x) / ( 16*x**4 - 272*x**3 + 1734*x**2 - 4913*x + 5220.625)

x = linspace(4.5,8.5, 1000)
y = Lsq(x)
yd= Lsqd(x)
ydd= Lsqdd(x)

plot([0, 8.5], [0, 0], '-k')
plot(x, y, '-r', x, yd, '-g', x, ydd, '-b')

#xoozi人生苦短, 证明就免了吧, 收获是用多项式类算有理函数的一阶和二阶导数
#用手算我铁定算错, 有理函数求跟我还不知道怎么用解析法球, 用循环逼近倒是会
