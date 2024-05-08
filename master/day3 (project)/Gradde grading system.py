#输入成绩
n1 = float(input("请输入成绩："))
#成绩分级
if n1 >= 60 and n1 < 70 :
    print("及格")
elif n1 >= 70 and n1 <= 90 :
    print("良好")
elif n1 >90 :
    print("优秀")
elif n1 < 60 :
    print("不及格") 