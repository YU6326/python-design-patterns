# 工厂方法模式定义了一个接口来创建对象，但具体实例化哪个类则是由它的子类决定的。

## 定义：工厂方法模式定义了一个用于创建对象的接口，让子类决定实例化哪一个类。
## 实现：通过抽象工厂类和子工厂来共同完成创建过程，每个具体工厂类只负责创建对应的一个产品。
## 优点：解决了简单工厂模式违反“开闭原则”的问题，增加产品的种类不需要修改已有的代码；
## 缺点：每增加一个产品就需要增加一个类，导致系统中类的个数成倍增加。

## 特点：多个工厂，一个产品类 常用


from abc import ABCMeta, abstractmethod

## 抽象产品类
class Section(metaclass=ABCMeta):
    @abstractmethod
    def describle(self):
        pass
## 具体产品类
class PersonalSection(Section):
    def describle(self):
        print('Personal Section')

class AlbumSection(Section):
    def describle(self):
        print('Album Section')

class PatentSection(Section):
    def describle(self):
        print('Patent Section')

class PublicationSection(Section) :
    def describle(self):
        print ('Publication Section')

# 创建Profile 抽象类
## 抽象工厂类
class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections=[]
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return [type(i).__name__ for i in self.sections]

    def addSections(self,section):
        self.sections.append(section)
## 具体工厂类
class Linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())

class Facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PublicationSection())
    
if __name__=='__main__':
    profile_type=input("which profile you'd like to create?")
    profile=eval(profile_type)()
    print('Create Profile...',type(profile).__name__) #type(*) 找*的类
    print('Profile has sections--',profile.getSections())