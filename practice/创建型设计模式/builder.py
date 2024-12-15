
## 特点：分步骤构建一个复杂对象

## 产品
class House:
    def __init__(self):
        self.foundation = None
        self.structure = None
        self.roof = None
        self.interior = None

    def __str__(self):
        return f"Foundation: {self.foundation}, Structure: {self.structure}, Roof: {self.roof}, Interior: {self.interior}"


from abc import ABC, abstractmethod

## 建造者
class HouseBuilder(ABC):
    @abstractmethod
    def build_foundation(self):
        pass

    @abstractmethod
    def build_structure(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_interior(self):
        pass

    @abstractmethod
    def get_house(self):
        pass

## 具体建造者
### 大厦
class MansionBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_foundation(self):
        self.house.foundation = "Concrete, reinforced with steel"

    def build_structure(self):
        self.house.structure = "Steel and Glass"

    def build_roof(self):
        self.house.roof = "Solar panel roof"

    def build_interior(self):
        self.house.interior = "Luxury interior with marble floors"

    def get_house(self):
        return self.house

### 普通房屋
class StandardHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_foundation(self):
        self.house.foundation = "Concrete"

    def build_structure(self):
        self.house.structure = "Wood and brick"

    def build_roof(self):
        self.house.roof = "Shingle roof"

    def build_interior(self):
        self.house.interior = "Basic interior with wooden floors"

    def get_house(self):
        return self.house


class HouseDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_foundation()
        self.builder.build_structure()
        self.builder.build_roof()
        self.builder.build_interior()
        return self.builder.get_house()


# 测试建造者模式
mansion_builder = MansionBuilder()
director = HouseDirector(mansion_builder)
mansion = director.construct_house()
print("Mansion:", mansion)

standard_builder = StandardHouseBuilder()
director = HouseDirector(standard_builder)
standard_house = director.construct_house()
print("Standard House:", standard_house)

