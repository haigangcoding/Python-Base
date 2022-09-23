# a * x + b = y

def a_line(a, b):
    def arg_y(x):
        return a*x+b
    return arg_y

line = a_line(3, 5)
print (line(10))
print (line(20))