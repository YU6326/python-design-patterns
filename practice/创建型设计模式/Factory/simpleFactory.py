# 允许接口创建对象，但不会暴露对象的创建逻辑。工厂可以帮助开发人员创建不同类型的对象，而不是直接将对象实例化。

## 实现：工厂类根据传入的参数决定创建哪个类的实例。
## 优点：客户端不需要知道具体产品的类名，只需要知道参数
## 缺点：当添加新产品时，需要修改工厂类的代码，违反了开闭原则。
## 适用场景：创建的对象少

## 存在目的：定义一个创建对象的接口
## 特点：一个工厂，一个产品类 有缺陷

from abc import ABCMeta, abstractmethod


## 抽象产品类
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass

## 具体产品类
class Dog(Animal):
    def do_say(self):
        print('Bhow Bhow!')

class Cat(Animal):
    def do_say(self):
        print('Meow Meow')

## 工厂类
class FroestFactory:
    def make_sound(self,obj):
        return eval(obj)().do_say()

if __name__=='__main__':
    ff=FroestFactory()
    ff.make_sound('Dog')