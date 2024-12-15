#       +------------------+        +-------------------+
#       |  Abstraction     |<>------|  Implementor      |
#       +------------------+        +-------------------+
#            ^                             ^
#            |                             |
#   +-----------------+          +-----------------------+
#   | RefinedAbstraction|        | ConcreteImplementor  |
#   +-----------------+          +-----------------------+
#   桥接：将“抽象”与“实现”分离开来

# 解耦抽象与实现：桥接模式将抽象部分和实现部分分离，使得两者可以独立变化。即可以独立地增加形状或颜色，而不需要修改其他类。
# 增加可扩展性：由于抽象和实现的分离，增加新的抽象和实现类变得更加容易，而不需要修改现有代码。
# 避免类的膨胀：如果没有桥接模式，在每个新增加的抽象或实现时，可能需要创建大量的子类。桥接模式通过组合来避免了这一问题。
# 与装饰器模式的区别：装饰者模式主要是用于“增加功能”，而桥接模式则是为了“分离变化维度”。
# 与策略模式的区别：策略模式是在运行时改变行为，而桥接模式主要用于分离实现与抽象部分，使得它们可以独立变化。

from abc import ABC, abstractmethod

class Color(ABC):
    @abstractmethod
    def fill_color(self):
        pass

class Red(Color):
    def fill_color(self):
        return "Red"

class Blue(Color):
    def fill_color(self):
        return "Blue"


class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color
        
    @abstractmethod
    def draw(self):
        pass
class Circle(Shape):
    def draw(self):
        return f"Drawing a circle with color {self.color.fill_color()}"

class Rectangle(Shape):
    def draw(self):
        return f"Drawing a rectangle with color {self.color.fill_color()}"

## client
# 创建不同颜色的对象
red = Red()
blue = Blue()

# 创建不同形状的对象
circle = Circle(red)
rectangle = Rectangle(blue)

# 输出绘制形状的结果
print(circle.draw())  # 输出: Drawing a circle with color Red
print(rectangle.draw())  # 输出: Drawing a rectangle with color Blue
