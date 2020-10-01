from math import sqrt, sin, cos, radians

print('Enter the number of the dimensions')
d = int(input())
print('Enter coordinates')
a = input().split()
for i in range(d):
    a[i] = int(a[i])
if d == 2:
    length = sqrt(a[0] ** 2 + a[1] ** 2)
    print(length)
    print('Enter a scalar to multiply by')
    x = int(input())
    b = [0] * d
    for i in range(d):
        b[i] = a[i] * x
    print(b)
    print('Enter the angle of rotation')
    alpha = radians(int(input()))
    b[0]= a[0] * cos(alpha) + a[1] * sin(alpha)
    b[1] = -1 * a[0] * sin(alpha) + a[1] * cos(alpha)
    print(b)
if d == 3:
    length = sqrt(a[0] ** 2 + a[1] ** 2 + a[2])
    print(length)
    print('Enter a scalar to multiply by')
    x = int(input())
    b = [0] * d
    for i in range(d):
        b[i] = a[i] * x
    print(b)
    print('Enter the angle of rotation')
    alpha = radians(int(input()))
    print('Enter the rotation axis')
    axis = input()
    if axis == 'x':
        b[0] = a[0]
        b[1] = a[1] * cos(alpha) - a[2] * sin(alpha)
        b[2] = a[1] * sin(alpha) + a[2] * cos(alpha)
    if axis == 'y':
        b[0] = a[0] * cos(alpha) + a[2] * sin(alpha)
        b[1] = a[1]
        b[2] = a[2] * cos(alpha) - a[0] * sin(alpha)
    if axis == 'z':
        b[0] = a[0] * cos(alpha) - a[1] * sin(alpha)
        b[1] = a[0] * sin(alpha) + a[1] * cos(alpha)
        b[2] = a[2]
    print(b)









