

def  fun1():
    global  x
    x='asdawesf'
    print(id(x))

    

def  fun2():
    #x='12313132123'  #这个是局部变量
    print(id(x))





fun1()
fun2()
print(id(x))