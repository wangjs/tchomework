#建造谷仓
#建造一个下部为圆柱, 上部为半球的谷仓(不包括底部), 就每平方英尺建造成本而言, 半球的成本是圆柱的两倍
#如果体积一定, 求最小成本的尺寸
#体积一定 V = h*pi*r**2 + (2*pi*r**3)/3 => h = V/(pi*r**2) - (2*r)/3
#面积     S = h*2*pi*r + 2*pi*r**2 = (2*V)/r -4*pi*r**2/3 + 2*pi*r**2
#           = 2*V/r + (2*pi*r**2)/3
#           = 2*V*r**-1 + 2*pi/3 * r**2
#         S'= -2V*r**-2 + 4*pi/3*r
#         2*V*r**-2 = 4*pi/3*r
#           3*V/pi = r**3

#         V = h*pi*r**2 + 2/3*pi*r**3
#         h = (V - 2/3*pi*r**3)/*(pi*r**2)
#           = V/(pi*r**2) - 2/3*r
#       
#         s = h*2*pi*r + 2*pi*r**2 = (V/(pi*r**2) - 2/3*r)*2*pi*r + 2*pi*r**2
#           = 2*V/r - (4*pi/3)*r**2 + 2*pi*r**2
#           = 2*V/r - (4*pi/3)*r**2 + (6*pi/3)*r**2
#           = 2*V/r + (2*pi/3)*r**2
#         s'= -2*V/r**2 + (4*pi/3)*r
#  2*V/r**2 = (4*pi/3)*r
#       (3*V/2pi) = r**3
#       r   = (3*V/2*pi)**1/3
#有问题, 哪里算错了
#xoozi, 看了官方答案, 答案中计算表面积是是用的s = h*2*pi*r + 4*pi*r**2
#我觉得是答案错了, 半球面积应该是2*pi*r**2啊
