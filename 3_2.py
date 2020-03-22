import numpy as np

x = [64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03]
y = [62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 129.44, 55.25, 104.84]

x = np.asarray(x)
y = np.asarray(y)
size = y.size
xavg = np.mean(x)
yavg = np.mean(y)

i = j = Sum = Sam = 0

while i < size:
    Sum = Sum+(x[i]-xavg)*(y[i]-yavg)
    i = i+1
while j < size:
    Sam = Sam+(x[j]-xavg)*(x[j]-xavg)
    j = j+1

w = Sum/Sam
b = yavg-w*xavg

print("w="+str(w))
print("b="+str(b))
