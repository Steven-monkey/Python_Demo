import re
import os

filename='students.txt'


# 输出界面化菜单
def menu():

    print('''
    ╔———————————————————学生信息管理系统——————————————-╗
    │                                               │
    │   =============== 功能菜单 ===============     |
    │                                               │
    │   1 录入学生信息                                │
    │   2 查找学生信息                                │
    │   3 删除学生信息                                │
    │   4 修改学生信息                                │
    │   5 排序                                       │
    │   6 统计学生总人数                               │
    │   7 显示所有学生信息                             │
    │   0 退出系统                                    │
    │  ===========================================  │
    │  说明：通过数字或↑↓方向键选择菜单                  │
    ╚———————————————————————————————————————————————╝
    ''')

#主函数
def main():
    ctrl=True                 #标记是否退出系统
    while(ctrl):              
        menu()                  #显示菜单
        option=input('请选择：')
        option_str=re.sub('\D',"",option)
        if option_str in ['0','1','2','3','4','5','6','7']:
            option_int=int(option_str)
            if option_int ==0:  #退出系统
                print('您已经退出学生信息管理系统。')
                ctrl=False
            elif option_int==1:
                insert()        #录入学生成绩信息
            elif option_int==2:
                search()        #查找学生成绩信息
            elif option_int==3:
                delete()        #删除学生成绩信息
            elif option_int==4:
                modify()        #修改学生成绩信息
            elif option_int==5:
                sort()          #排序
            elif option_int==6:
                total()         #统计学生总数
            elif option_int==7:
                show()          #显示所以学生信息

'''1 录入学生信息'''
#录入学生成绩信息
def insert():
    studentList=[]
    mark=True
    while mark:
        id=input('请输入ID（如101）：')
        if not id:
            break
        name=input('请输入名字：')
        if not name:
            break
        try:
            english=int(input('请输入英语成绩：'))
            python=int(input('请输入python成绩：'))
            c=int(input('请输入c语言成绩：'))
        except:
            print('输入值无效，不是整型数值...重新录入信息。')
            continue
        student={
            'id':id,
            'name':name,
            'english':english,
            'python':python,
            'c':c
            }
        studentList.append(student)
        inputMark=input('是否继续添加?(y/n):')
        if inputMark =='y':
            mark=True
        else:
            mark=False
    save(studentList)
    print('学生信息录入完毕！')

'''2 查找学生信息'''
#查找学生成绩信息
def search():
    mark=True
    student_query=[]
    while mark:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按ID查询输入1；按姓名查找输入2：')
            if mode=='1':
                id=input('请输入学生ID：')
            elif mode=='2':
                name=('请输入学生姓名：')
            else:
                print('您的输入有误，请您重新输入...')
                search()
            with open(filename,'r') as file:
                student=file.readlines()
                for list in student:
                    d=dict(eval(list))
                    if id != "":
                        if d['id']==id:
                            student_query.append(d)
                    elif name != "":
                        if d['name']==name:
                            student_query.append(d)
                show_student(student_query)
                student_query.clear()       #清空列表
                inputMark=input('是否继续查询？（y/n）：')
                if inputMark=='y':
                    mark=True
                else:
                    mark=False
        else:
            print('暂未保存数据信息...')
            return

'''3 删除学生信息'''
#删除学生成绩信息
def delete():
    mark=True
    while mark:
        studentId=input('请输入要删除的学生ID：')
        if studentId != "":
            if os.path.exists(filename):
                with open(filename,'r') as rfile:
                    student_old=rfile.readlines()
            else:
                student_old=[]
            ifdel=False
            if student_old:                     #如果存在学生信息
                with open(filename,'w') as wfile:
                    d={}
                    for list in student_old:
                        d=dict(eval(list))      #字符串转字典
                        if d['id']!=studentId:
                            wfile.write(str(d)+'\n')
                        else:
                            ifdel=True
                    if ifdel:
                        print('ID为%s的学生信息已经被删除...'%studentId)
                    else:
                        print('没有找到ID为%s的学生信息...'%studentId)
            else:
                print('无此学生信息...')
                break
            show()                              #显示全部学生信息
            inputMark=input('是否继续删除？（y/n）')
            if inputMark=='y':
                mark=True
            else:
                mark=False

'''4 修改学生信息'''
#修改学生信息
def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r') as rfile:
            student_old=rfile.readlines()
    else:
        return
    studentid=input('请输入要修改的学生ID：')
    with open(filename,'w') as wfile:
        for student in student_old:
            d=dict(eval(student))
            if d['id']==studentid:
                print('找到了这名学生，可以修改他的信息！')
                while True:
                    try:
                        d['name']=input('请输入姓名：')
                        d['english']=int(input('请输入英语成绩：'))
                        d['python']=int(input('请输入Python成绩：'))
                        d['c']=int(input('请输入C语言成绩：'))
                    except:
                        print('您的输出有误，请重新输入...')
                    else:
                        break
                student=str(d)          #将字典转换成字符串
                wfile.write(student+'\n')
                print('修改成功')
            else:
                wfile.write(student)    #将修改的写入文件
    mark=input('是否继续修改其他学生信息？（y/n）：')
    if mark=='y':
        modify()        

'''5 排序'''
#排序
def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r') as file:
            student_old=file.readlines()
            student_new=[]
        for list in student_old:
            d=dict(eval(list))
            student_new.append(d)
    else:
        return
    ascORdesc=input("请选择（0升序；1降序）：")
    if ascORdesc=='0':
        ascORdescBool=False
    elif ascORdesc=='1':
        ascORdescBool=True
    else:
        print('您的输入有误，请重新输入！')
        sort()
    mode=input('请选择排序方式（1按英语成绩排序；2按python成绩排序；3按c语言成绩排序；0按总成绩排序）：')
    if mode=='1':
        student_new.sort(key=lambda x:x['english'],reverse=ascORdescBool)
    elif mode=='2':
        student_new.sort(key=lambda x:x['python'],reverse=ascORdescBool)
    elif mode=='3':
        student_new.sort(key=lambda x:x['python'],reverse=ascORdescBool)
    elif mode=='0':
        student_new.sort(key=lambda x:x['english']+x['python']+x['c'],reverse=ascORdescBool)
    else:
        print('您的输入有误，请重新输入！')
        sort()
    show_student(student_new)

'''6 统计学生总人数'''
#统计学生总数
def total():
    if os.path.exists(filename):
        with open(filename,'r') as rfile:
            student_old=rfile.readlines()
            if student_old:
                print('一共有%d名学生！'% len(student_old))
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存数据信息...')

'''7 显示所有学生信息'''
#显示所以信息
def show():
    student_new=[]
    if os.path.exists(filename):
        with open(filename,'r') as rfile:
            student_old=rfile.readlines()
        for list in student_old:
            student_new.append(eval(list))
        if student_new:
            show_student(student_new)
    else:
        print('暂未保存数据信息...')

#将保存在列表中的学生信息显示出来
def show_student(studentList):
    if not studentList:
        print('(o@.@o  无数据信息 （o@.@o）')
        return
    #定义标题显示格式
    format_title="{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format('ID','name','英语成绩','Python成绩','C语言成绩','总成绩'))
    #定义具体内容显示格式   数字表示所占宽度，^表示居中显示  \t表示添加一个制表符
    format_data="{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in studentList:
        print(
            format_data.format(
                info.get('id'),
                info.get('name'),
                str(info.get('english')),
                str(info.get('python')),
                str(info.get('c')),
                
                str(info.get('c')+info.get('python')+info.get('english')).center(12)))

'''保存学生信息'''
#将学生信息保存到文件
def save(student):
    try:
        students_txt=open(filename,'a')
    except Exception as e:
        students_txt=open(filename,'w')
    for info in student:
        students_txt.write(str(info)+'\n')
    students_txt.close()

#执行函数
if __name__=='__main__':
    main()