    #   +--------------------+
    #   |     Client         |
    #   +--------------------+
    #            |
    #            ▽
    #   +--------------------+
    #   |    Target Interface| 目标接口：客户端希望使用的接口
    #   +--------------------+
    #            △
    #            |
    #   +--------------------+    +-------------------+
    #   |     Adapter        |——>|    Adaptee        | ##源接口
    #   +--------------------+    +-------------------+

## 适配器：实现了目标接口并且包含对源接口的引用，将源接口的调用转换为目标接口的调用
## 目的：解决接口不兼容问题

# target interface
class Printer:
    def print_document(self, document: str):
        pass

# adaptee
class OldPrinter:
    def print(self, content: str):
        print(f'Printing using old printer:{content}')

# adapter
class PrintAdapter(Printer):
    def __init__(self,old_printer):
        self.old_printer=old_printer
    
    def print_document(self,document: str):
        #转换
        self.old_printer.print(document)
    
class Client:
    def __init__(self,printer):
        self.printer=printer
    
    def print(self,document:str):
        self.printer.print_document(document)

old_printer=OldPrinter()
adapter=PrintAdapter(old_printer)
client=Client(adapter) #因为adapter 实现了target interface 接口
client.print('hello, Adapter Pattern!')

