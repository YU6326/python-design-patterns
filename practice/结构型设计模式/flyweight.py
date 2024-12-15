# +--------------------+        +--------------------+        +--------------------+        +--------------------+
# |     Flyweight      |<-------| ConcreteFlyweight  |<-------|  FlyweightFactory  |<-------|      Client        |
# +--------------------+        +--------------------+        +--------------------+        +--------------------+
# | + operation(extr): |        | - intr: Any        |        | - flyweights: dict |        | - extr: Any        |
# |   void             |        | + operation(extr): |        | + get_flyweight(   |        | + use_flyweight(): |
# |                    |        |   void             |        |   key): Flyweight  |        |   void             |
# +--------------------+        +--------------------+        | + create_flyweight(|        +--------------------+
#                                                            |   key): Flyweight  |
#                                                            +--------------------+

## 通过共享相同的对象减少内存使用和对象创建的开销
## 核心思想：将对象的状态分为内部状态和外部状态
### 内部状态：有限的，可列的，存储在享元内部，不随环境改变
### 外部状态：无限的，不可列的，存储在客户端，由客户端传给享元对象

class TreeType:
    """享元类，表示树的类型（内部状态）"""
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x, y):
        """绘制树时需要外部状态（位置）"""
        print(f"Drawing {self.name} tree at ({x}, {y}) with color {self.color} and texture {self.texture}")


class TreeFactory:
    """享元工厂类，管理树类型的共享"""
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        key = (name, color, texture)
        if key not in cls._tree_types:
            cls._tree_types[key] = TreeType(name, color, texture)
            print(f"Created new TreeType: {key}")
        else:
            print(f"Reusing existing TreeType: {key}")
        return cls._tree_types[key]


class Tree:
    """具体的树类，包含位置（外部状态）和树类型（享元）"""
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        self.tree_type.draw(self.x, self.y)


class Forest:
    """客户端类，管理树的集合"""
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self):
        for tree in self.trees:
            tree.draw()


# 使用示例
forest = Forest()
forest.plant_tree(10, 20, "Oak", "Green", "Rough")
forest.plant_tree(15, 25, "Oak", "Green", "Rough")
forest.plant_tree(20, 30, "Pine", "Dark Green", "Smooth")
forest.draw()
