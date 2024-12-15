##  通过复制现有对象来创建新对象

## 浅拷贝：创建一个新的对象，但不复制嵌套对象的内容。
## 深拷贝：递归复制所有嵌套对象，创建一个完全独立的副本。

import copy
from abc import ABC, abstractmethod

# 抽象原型类 （拷贝接口）
class Prototype(ABC):
    
    @abstractmethod
    def clone(self):
        pass

# 具体原型类
class ConcretePrototype1(Prototype):
    
    def __init__(self, value, nested_object):
        self.value = value
        self.nested_object = nested_object
    
    def clone(self, deep=False):
        if deep:
            return copy.deepcopy(self)
        else:
            return copy.copy(self)
    
    def __str__(self):
        return f"ConcretePrototype1(value={self.value}, nested_object={self.nested_object})"

# 嵌套对象
class NestedObject:
    def __init__(self, attribute):
        self.attribute = attribute
    
    def __str__(self):
        return f"NestedObject(attribute={self.attribute})"

# 客户端
# 创建原型对象
nested_obj = NestedObject("Initial Attribute")
prototype = ConcretePrototype1(10, nested_obj)

# 浅拷贝
shallow_copy = prototype.clone(deep=False)
# 深拷贝
deep_copy = prototype.clone(deep=True)

# 输出原型和副本的状态
print("Original Prototype:", prototype)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)

# 修改嵌套对象的属性
nested_obj.attribute = "Modified Attribute"

print("\nAfter modifying the nested object:")
print("Original Prototype:", prototype)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)



