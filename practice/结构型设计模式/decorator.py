from abc import ABC, abstractmethod
    #   +-------------------+        +-------------------+
    #   |     Component     |<>------|     Decorator     |
    #   +-------------------+        +-------------------+
    #            △                           △
    #            |                           |
    # +---------------------+       +----------------------+
    # | ConcreteComponent    |       | ConcreteDecorator    |
    # +---------------------+       +----------------------+

# 组件接口
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass

# 具体组件
class SimpleCoffee(Coffee):
    def cost(self):
        return 5  # 简单咖啡的价格

# 装饰器基类
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee  # 组合具体的咖啡对象

    @abstractmethod
    def cost(self):
        pass

# 具体装饰器 1: 加奶
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2  # 加奶的价格

# 具体装饰器 2: 加糖
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1  # 加糖的价格

# 客户端代码
coffee = SimpleCoffee()
print(f"Simple Coffee cost: ${coffee.cost()}")

# 使用装饰器
milk_coffee = MilkDecorator(coffee)
print(f"Milk Coffee cost: ${milk_coffee.cost()}")

sugar_milk_coffee = SugarDecorator(milk_coffee)
print(f"Milk Coffee with Sugar cost: ${sugar_milk_coffee.cost()}")
