a = input("Enter Length of Race in Kilometers: ")
b = input("Enter Minutes: ")
c = input("Enter Seconds: ")
x = 1.61
y = 60
d = (int(a) / x)
e = (int(b) / y)
f = (int(c) / y)
g = (int(b) + int(c))
h = (int(a) / int(g))
print(h)