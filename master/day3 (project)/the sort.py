#从键盘录入三个数据
print("请分别输入三个数据：")
n1 = float(input(""));n2 = float(input(""));n3 = float(input(""))
#将三个数据分选
if n1>n2 and n1>n3:#n1为最大的情况
    first = n1
    
    if n2>n3:#比较 n2，n3 
        second = n2;thirdly = n3
    else:
        sceond = n3;thirdly = n2

else: 
    if n2>n1 and n2>n3:#n2为最大的情况
        first = n2
        if n1>n3 :
            sceond = n1;thirdly = n3
        else:
            sceond = n3;thirdly = n1

if n3>n1 and n3>n2 :
    first = n3
    if n1>n2:
        second = n1;thirdly = n2
    else:
        second = n2;thirdly = n1    
print(f'第一，第二，第三分别是：{first,second,thirdly}')




