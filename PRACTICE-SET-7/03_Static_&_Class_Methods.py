class MathUtils:
    def __init__(self):
        pass
    @staticmethod
    def add(a, b):
        return a+b
    @classmethod
    def description(cls):
        print("This is a utility class for math operations.")

m = MathUtils()
print(MathUtils.add(10, 20))
MathUtils.description()
