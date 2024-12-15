
## 对产品进行分组，根据继承抽象工厂中的方法创建同组不同具体产品对象。
## 适用：多个类型的多个产品
## 特点：多个工厂，多个产品类 关注的是一个产品家族 罕见

from abc import ABCMeta, abstractmethod
 
# 创建披萨工厂抽象类
class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def createVegPizza(self):
        pass
 
    @abstractmethod
    def createNonVegPizza(self):
        pass
 
# 创建印式披萨工厂类
class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()
 
    def createNonVegPizza(self):
        return ChickenPizza()
 
# 创建美式披萨类
class USPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanVegPizza()
 
    def createNonVegPizza(self):
        return HamPizza()
 
# 创建素食披萨抽象类
class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, VegPizza):
        pass
 
# 创建非素食披萨抽象类
class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VegPizza):
        pass
 
# 创建美味蔬菜披萨类，准备美味蔬菜披萨
class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print('Prepare ', type(self).__name__)
 
# 创建鸡肉披萨类，将素食披萨搭配上鸡肉
class ChickenPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Chicken on ", type(VegPizza).__name__)
 
# 创建墨西哥蔬菜披萨类
class MexicanVegPizza(VegPizza):
    def prepare(self):
        print('Prepare ', type(self).__name__)
 
# 创建火腿披萨类，将素食披萨搭配上火腿
class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Ham on ", type(VegPizza).__name__)
 
# 创建披萨商店类
class PizzaStore:
    def __init__(self):
        pass
 
    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory  # 实例化披萨工厂
            self.NonVegPizza = self.factory.createNonVegPizza()  # 实例化素食披萨
            self.VegPizza = self.factory.createVegPizza()  # 实例化非素食披萨
            self.VegPizza.prepare()  # 准备素食披萨
            self.NonVegPizza.serve(self.VegPizza)  # 将肉/火腿搭配到素食披萨上
 
 
if __name__ == '__main__':
    pizza = PizzaStore()  # 实例化披萨商店
    pizza.makePizzas()  # 制作披萨

