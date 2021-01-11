class Test:
    def __init__(self):
        attrs = ["name", "age", "mother", "father"]
        for attr in attrs:
            self.attr = attr


obj = Test()
print(obj.__dict__)