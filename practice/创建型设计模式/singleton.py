import time
#这里使用__new__来实现单例模式
class Singleton(object):
    def __new__(cls): #cls:类 self:对象
        if not hasattr(cls,'_instance'): #没有任何实例
            father=super(Singleton,cls) #获取父类father即object
            cls._instance=father.__new__(cls)
        return cls._instance

# super的基本参数：子类类名，子类实例。返回父类。

class Singleton2(object):
    _instance=None #类变量，即静态变量
    def __new__(cls):
        if cls._instance is None: #用is的原因:None 在python中是个单例对象，一个变量如果是None，它一定和None指向同一个内存地址，用is更快，True/False 同理
                cls._instance=object.__new__(cls)
        return cls._instance


# __init__不是真正意义上的构造函数
# __new__才是构造函数
# __new__方法是创建实例的方法，是静态方法
# __init__方法是在对象创建好之后的初始化方法，是实例方法

# 绑定(bound)和未绑定(unbound)的区别

class A:
    def test(self):
        print('test')

a=A()
A.test(a) #A.test 返回一个function对象， 是一个未绑定函数，调用时需要传对象
a.test() #a.test 返回一个bound method对象，是一个绑定函数，调用时不需要再传入对象
# 可以看出，所谓绑定，就是把调用函数的对象，绑定到函数的第一个参数上。