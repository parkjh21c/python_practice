x = [6,14,3,22,9,11,12,5,18,24,15,17]
y = [2.8,3.2,3.1,3.6,3.0,3.3,3.4,2.7,3.1,3.8,3.0,3.9]

x_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

x_ = 13
y_ = 3.24*100

total = 0
total_y = 0

for i in range(12):
    x_x[i] = x[i] - x_
    y_y[i] = y[i]*100 - y_

print(x_x)
print(y_y)

for i in range(12):
    total = total + x_x[i]*y_y[i]

print(total)

for i in range(12):
    total_y = total_y + y_y[i]**2

total_y = total_y/10000
print(total_y)
