"""
** Directions: **
For each of the following problems, trace 
through the code and keep track of the value 
of each variable at critical points in the code.

Write the final value of each variable in the 
space provided after each problem.
"""

# Problem 1
x = 10
y = 20
z = 30

for i in range(5):
    x += i
    y -= i
    if x < y:
        z *= i
"""
Answer 1 
Final Values:
x --> 
y -->
z --> 
"""


# Problem 2
num = 10
num = num + num / 3
num *= num % 4

if num > 10:
    num = num - 3
else:
    num = num + 2
"""
Answer 2
Final Values:
num --> 
"""


# Problem 3
result = 0
base = 3

for i in range(1, 11):
    if i % 2 == 0:
        result += base ** i
"""
Answer 3 
Final Values:
result --> 
base ----> 
"""


# Problem 4
result = ""
num = 10

for i in range(num):
    if i % 3 == 0:
        result += "A"
    elif i % 3 == 1:
        result += "B"
    else:
        result += "C"
"""
Answer 4 
Final Values:
result --> 
num ----->
"""


# Problem 5
x = 15
y = x * 2
z = int(y / 3)

if z % 2 == 0:
    x = z + 2
else:
    x = z - 2

x = int(x / 2) if y > x else x * 2
"""
Answer 5
Final Values:
x --> 
y -->
z --> 
"""