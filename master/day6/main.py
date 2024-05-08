#print(sep="")
#spe=""是用来控制分割符的  ""里面填入一个希望字符串之间出现的分隔符
""" 函数的参数是调用函数时提供给函数的参数
返回值是函数执行完的结果 """

#def 函数名():
#   函数体
#   return 返回值
def say_hi():
    print("Hi")
#函数在执行到return时函数体立即结束执行，return下面的东西不在执行
#return none = return 0 在python中要写 return none或只写return

def goodmoring():
    """ 输出一句goodmoring """
    print("goodmoring")
#如果在函数体的开头写一个块注释，那么在代码提示中就会出现   

goodmoring()
say_hi()