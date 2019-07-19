'''
函数：对功能的封装

优点
1.简化代码，增加重复使用的程度
2.如果想修改某些功能或者调试某个BUG
'''


'''
定义函数:
def 函数名(参数列表.)：
    语句
    return表达式


def:函数代码以def关键字开始
函数名：遵循标识符规则
参数列表：（参数1，参数2......）:任何传入函数的参数和变量必须放在括号内，用逗号隔开。函数从函数的调用者那里获取信息
冒号：函数内容以冒号开始，并且缩进
语句: 函数的功能
return：结束函数，并返回信息给函数的调用者
表达式：为返回给函数的调用者
'''
def myPrint():
    print("sunck is a good man")
    print("sunck is a nice man")

'''
函数的调用
格式：函数名（参数列表）

函数名：使用的功能的函数名字
参数列表：函数的调用者给函数传递的信息
本质：实参给形参赋值的过程
'''
x=int(input())
def fun(x):
    x*3+45

