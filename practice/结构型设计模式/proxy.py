# 它提供了一个代理对象来控制对目标对象的访问。代理可以在目标对象之前进行一些操作，如控制访问权限、延迟实例化或添加额外的功能。

## 单位的“门卫”

# +--------------------+        +--------------------+
# |      Subject       |<-------|   RealSubject      |
# +--------------------+        +--------------------+
# | + request(): void  |        | + request(): void  |
# +--------------------+        +--------------------+
#           ▲
#           |
#           |
# +--------------------+
# |       Proxy        |
# +--------------------+
# | - _real_subject:   |
# |   RealSubject      |
# | + request(): void  |
# | + _check_access(): |
# |   bool             |
# | + _log_access():   |
# |   void             |
# +--------------------+

# Subject（抽象主题接口）：定义代理和实际对象的共有接口。
# RealSubject（真实对象）：执行实际操作的对象。
# Proxy（代理对象）：包含对真实对象的引用，通过真实对象实现抽象接口，并对其访问进行控制。

# 虚拟代理：延迟加载大对象，提升性能。
# 保护代理：控制对对象的访问权限。
# 智能引用：在访问对象时增加日志或跟踪功能。

from abc import ABC, abstractmethod

class Subject(ABC):
    """抽象主题接口"""
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    """真实对象"""
    def request(self):
        print("RealSubject: Handling request.")

class Proxy(Subject):
    """代理对象"""
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        if self._check_access():
            self._real_subject.request()
            self._log_access()

    def _check_access(self):
        print("Proxy: Checking access before forwarding request.")
        return True

    def _log_access(self):
        print("Proxy: Logging the access to RealSubject.")

# 客户端代码
def client_code(subject: Subject):
    subject.request()

print("Client: Executing with a real subject:")
real_subject = RealSubject()
client_code(real_subject)

print("\nClient: Executing with a proxy:")
proxy = Proxy(real_subject)
client_code(proxy)
