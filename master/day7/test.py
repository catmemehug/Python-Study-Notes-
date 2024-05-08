years = input("请输入年月日,并用空格分开：")
number = years.split()#利用.split函数将输入的一组数据切成三个变量
year = int(number[0])
month = int(number[1])
day = int(number[2])
if month == 1:
        year -= 1
        month == 13
elif month == 2:
        year -= 1
        month == 14
#第二步：通过录入的年月计算这天星期几
#计算公式：
w = (day+2*month+3*(month+1)//5+year+year//4-year//100+year//400) % 7+1 
print(f'这天是星期{w}')
