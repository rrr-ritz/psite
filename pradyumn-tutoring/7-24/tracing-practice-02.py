"""
** Directions: **
For each of the following problems, trace 
through the code and keep track of the value 
of each variable at critical points in the code.

Write the final value of each variable in the 
space provided after each problem.
"""

# Problem 1
p = 2
q = 3
r = 5

for i in range(3, 7):
    p += i * 2
    q -= i
    if p > q:
        r *= i
    else:
        r = r / i
"""
Answer 1
Final Values:
p -->
q -->
r --> 
"""


# Problem 2
num = 10
num = num * num / 5
num *= num % 7

if num > 100:
    num = num - 50
elif num == 100:
    num = num * 2
else:
    num = num + 30
"""
Answer 2
Final Values:
num --> 
"""


# Problem 3
x = 1
y = 10
z = 100

for i in range(3,8):
    x += y
    y -= i
    if x < y:
        z *= i
    else:
        z = z / i
"""
Answer 3 
Final Values:
x --> 
y -->
z --> 
"""


# Problem 4
a = 10
b = 15
c = a + b

for i in range(3):
    a += i
    b -= i * 2
    c += a * b
"""
Answer 4
Final Values:
a --> 
b -->
c --> 
"""


# Problem 5
a = 2
b = 3
c = 5

for i in range(4):
    a += i ** 2
    b += i ** 3
    c += a * b
"""
Answer 5
Final Values:
a --> 
b -->
c --> 
"""


# Problem 6
x = 20
y = x * 4
z = int(y / 5)

if z % 2 == 0:
    x = z + 5
else:
    x = z - 5

x = int(x / 4) if y > x else x * 4
"""
Answer 6
Final Values:
x --> 
y -->
z --> 
"""


# Problem 7
result = 0
base = 4

for i in range(1, 15):
    if i % 3 == 0:
        result += base ** (i / 2)
"""
Answer 7 
Final Values:
result --> 
base ----> 
"""


# Problem 8
count = 5
message = ""

for i in range(1, count * 2, 2):
    if i % 3 == 0:
        message += "Fizz"
    else:
        message += "Buzz"
    count += 2
"""
Answer 8
Final Values:
count -->
message -->
"""


# Problem 9
start = 10
step = start + 5
end = step * start

step = end if end > 100 else start
start = end % step
"""
Answer 9
Final Values:
start -->
step -->
end -->
"""


# Problem 10
num1 = 10
num2 = num1 ** 2 / 2
num3 = (num1 * num2) % 7

if num3 > 8:
    num3 = num3 - 4
else:
    num3 = num3 + 3
"""
Answer 10
Final Values:
num1 -->
num2 -->
num3 -->
"""
