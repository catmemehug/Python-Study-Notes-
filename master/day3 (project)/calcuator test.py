#声明变量 
n1 = float(input("请输入："))#输入第一个数据
n2 = input("请输入运算符：")#录入运算符
n3 = float(input("请输入"))#输入第三个数据
#选择运算符，并对应运算逻辑
if n2 == '+' :
    print(f'结果为:{n1+n3}')
elif n2 == '-' :
    print(f'结果为:{n1-n3}')
elif n2 == '*' :
    print(f'结果为:{n1*n3}')
elif n2 == '/' :
    print(f'结果为:{n1/n3}')        