import matplotlib.pyplot as plt
import tensorflow as tf

boston_housing = tf.keras.datasets.boston_housing
(train_x, train_y), (_, _) = boston_housing.load_data(test_split=0)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
titles = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B-1000", "LSTAT", "MEDV"]

plt.figure()
for i in range(13):
    print(str(i)+" -- "+titles[i])
a = int(input("please input"))
plt.scatter(train_x[:, a], train_y)
plt.xlabel(titles[a])
plt.ylabel("Price($1000's)")
plt.title(str(a+1)+"."+titles[a]+"-Pirce")
plt.show()
