import math
a = float(input('请输入系数a：'))
b = float(input('请输入系数b：'))
c = float(input('请输入常数c：'))
if a == 0:
    print("系数a不能为0")
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("无实数解")
    elif delta == 0:
        print("有一个实数解：")
        print((-b+math.sqrt(delta))/(2*a))
    else:
        print("有两个实数解")
        print((-b+math.sqrt(delta))/(2*a))
        print((-b-math.sqrt(delta))/(2*a))