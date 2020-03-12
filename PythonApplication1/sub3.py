import random as rd
import pandas as pd



# 两位数加法
def sub1():
    for i in range(40):
        s = "%d+%d=" % (rd.randint(10, 100), rd.randint(10, 100))
        print(s)


# 两位数减法
def sub2():
    i = 0
    while i < 40:
        s = "%d-%d" % (rd.randint(10, 100), rd.randint(10, 100))
        if eval(s) > 0:
            print(s, end='=\n')
            i = i + 1


# 两位数减法
def sub3():
    i = 0
    while i < 40:
        s = "%d-%d" % (rd.randint(10, 100), rd.randint(10, 100))
        if eval(s) > 0 and eval(s) < 100:
            print(s, end='=\n')
            i = i + 1


# 个位乘法
def sub4():
    for i in range(40):
        s = "%dx%d" % (rd.randint(1, 9), rd.randint(1, 9))
        print(s, end='=\n')


# 个位乘法
def sub5():
    for i in range(40):
        a = rd.randint(3, 9)
        b = rd.randint(3, 9)
        s = "%2d ÷%2d" % (a * b, b)
        print(s, end='=\n')


# 两位加法
def sub6():
    for i in range(40):
        a = rd.randint(1, 9)
        b = rd.randint(1, 9)
        c=rd.randint(1, 9)
        d=rd.randint(1, 9)
        s = "%d%d + %d%d" % (a,b,c,d)
        print(s, end='=\n')



# 20以内加法
def sub7():
    for i in range(40):
        a = rd.randint(6, 19)
        b = rd.randint(8, 19)
        c=rd.randint(1, 9)
        d=rd.randint(1, 9)
        s = "%d + %d" % (a,b)
        print(s, end='=\n')


# 两位数加法，不进位
# 两位数加法，进位
# 两位数加法，不退位
# 两位数加法，退位


if __name__ == '__main__':
    sub7()
