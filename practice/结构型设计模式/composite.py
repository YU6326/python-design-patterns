from abc import ABC, abstractmethod
# 它允许你将对象组合成树形结构来表示“部分-整体”的层次结构。它使得客户端可以以一致的方式对待单个对象和组合对象，从而实现了对树状结构的透明操作。

## 单个对象和组合对象有一致的方法
# Component 接口
class Graphic(ABC):
    @abstractmethod
    def render(self):
        pass

# Leaf 节点
class Circle(Graphic):
    def render(self):
        print("Rendering a Circle")

class Rectangle(Graphic):
    def render(self):
        print("Rendering a Rectangle")

# Composite 节点
class CompositeGraphic(Graphic):
    def __init__(self):
        self._children = []

    def add(self, graphic):
        self._children.append(graphic)

    def remove(self, graphic):
        self._children.remove(graphic)

    def render(self):
        print("Rendering a Composite Graphic")
        for child in self._children:
            child.render()

# 客户端代码
circle1 = Circle()
circle2 = Circle()
rectangle = Rectangle()

composite = CompositeGraphic()
composite.add(circle1)
composite.add(rectangle)

nested_composite = CompositeGraphic()
nested_composite.add(circle2)
nested_composite.add(composite)

nested_composite.render()
