import tkinter as tk

class Model:
    def __init__(self):
        self._data = 0
        self._observers = []

    def set_data(self, value):
        self._data = value
        self.notify_observers()

    def get_data(self):
        return self._data

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._data)



class View(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.label = tk.Label(self, text="0")
        self.label.pack()

        self.button = tk.Button(self, text="Increase", command=None)  # command 将由控制器设置
        self.button.pack()

        self.pack()

    def set_controller(self, controller):
        self.button.config(command=controller.increase_data)

    def update(self, data):
        self.label.config(text=str(data))

# multiview
class GraphicalView(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.canvas = tk.Canvas(self, width=200, height=50)
        self.canvas.pack()
        self.pack()

    def update(self, data):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, data * 10, 50, fill="blue")


class Controller:
    def __init__(self, model):
        self.model = model

    def increase_data(self):
        current_value = self.model.get_data()
        self.model.set_data(current_value + 1)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("MVC Example")

    # 实例化 Model
    model = Model()

    # 实例化 View
    view = View(root)
    graphical_view=GraphicalView(root)
    

    # 实例化 Controller
    controller = Controller(model)

    # 连接 Model 和 View
    model.add_observer(view)
    model.add_observer(graphical_view)

    # 连接 View 和 Controller
    view.set_controller(controller)

    root.mainloop()